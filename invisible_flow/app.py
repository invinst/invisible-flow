import pdb
from io import BytesIO
from logging import getLogger
from logging.config import dictConfig

import pandas as pd
from flask import render_template, Response

from invisible_flow.app_factory import app
from invisible_flow.copa.mapper import Mapper
from invisible_flow.copa.allegation_saver import AllegationSaver
from invisible_flow.copa.loader import Loader
from invisible_flow.copa.officer_saver import OfficerSaver
from invisible_flow.copa.saver import Saver, strip_zeroes_from_beat_id, cast_col_to_int
from invisible_flow.globals_factory import GlobalsFactory  # noqa: F401
from invisible_flow.api.copa_scrape import scrape_data, scrape_allegation_data, scrape_officer_data, scrape_crids
from invisible_flow.copa.sorter import Sorter
from invisible_flow.transformers.allegation_transformer import AllegationTransformer
from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer

# Logging configuration
from invisible_flow.transformers.officer_transformer import OfficerTransformer

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

logger = getLogger(__name__)


@app.route('/status', methods=['GET'])
def status():
    return 'ok', 200


@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def index(path):
    return render_template('index.html')


@app.route('/copa_scrape_deprecated', methods=['GET'])
def copa_scrape_deprecated():
    scraped_data = scrape_data()

    transformer = CopaScrapeTransformer()
    transformer.transform(scraped_data)
    transformed_data = transformer.get_transformed_data()

    loader = Loader()
    loader.load_into_db(transformed_data)

    saver = Saver()

    saver.save_to_csv(strip_zeroes_from_beat_id(loader.get_allegation_matches()), "match_data.csv")

    saver.save_to_csv(strip_zeroes_from_beat_id(loader.get_new_allegation_data()), "new_allegation_data.csv")

    saver.save_to_csv(cast_col_to_int(loader.new_officer_unknown_data, "data_officerallegation_id"),
                      "new_officer_unknown.csv")
    saver.save_to_csv(loader.new_officer_allegation_data, "new_officer_allegation.csv")

    # do further processing on officer unknown
    return Response(status=200, response='Success')


@app.route('/copa_scrape', methods=['GET'])
def copa_scrape():
    sorter = Sorter()
    mapper = Mapper()

    scraped_crids = scrape_crids()
    scraped_crids_df = pd.read_csv(BytesIO(scraped_crids), encoding='utf-8', sep=",", dtype=str)
    crids = list(scraped_crids_df['log_no'].values)
    # why go from df to list to set(in copa_scraper)? why not just go from df to set?

    sorter.split_crids_into_new_and_old(crids, mapper.query_existing_crid_table())

    allegation_scraper(sorter, mapper)
    officer_scraper(sorter, mapper)
    return Response(status=200, response='Success')


def allegation_scraper(sorter: Sorter, mapper: Mapper):
    scraped_data = scrape_allegation_data()
    scraped_df = pd.read_csv(BytesIO(scraped_data), encoding='utf-8', sep=",", dtype=str)

    new_allegation_rows = sorter.get_new_copa_rows(scraped_df)

    # query db for data allegations associated with existing crids -- convert to df
    existing_allegation_rows = mapper.get_existing_allegation_data()

    allegation_transformer = AllegationTransformer()
    transformed_new_allegation_rows = allegation_transformer.transform(new_allegation_rows)

    mapper.load_allegation_into_db(transformed_new_allegation_rows)

    # save new crid rows to csv
    allegation_saver = AllegationSaver()
    allegation_saver.save_allegation_to_csv(new_allegation_rows, "new_allegation_data.csv")

    # save existing crids to csv
    allegation_saver.save_allegation_to_csv(existing_allegation_rows, "existing_allegation_data.csv")

    # Put new crids in db
    old_crids = sorter.get_old_crids()
    new_crids = sorter.get_new_crids()

    mapper.save_new_crids_to_db(old_crids, new_crids)


def officer_scraper(sorter: Sorter, mapper: Mapper):
    scraped_data = scrape_officer_data()
    scraped_df = pd.read_csv(BytesIO(scraped_data), encoding='utf-8', sep=",", dtype=str)

    new_officer_rows = sorter.get_new_copa_rows(scraped_df)

    # query db for officer data associated with existing crids -- convert to df
    existing_officer_rows = mapper.get_existing_officer_data()

    officer_transformer = OfficerTransformer()
    transformed_new_officer_data = officer_transformer.transform(new_officer_rows)

    # Load transformed rows into DB (Maybe omit 8/5/20)
    mapper.load_officer_into_db(transformed_new_officer_data)

    officer_saver = OfficerSaver()
    officer_saver.save_officer_to_csv(existing_officer_rows, transformed_new_officer_data)

if __name__ == '__main__':
    app.run(debug=True)
