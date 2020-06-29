from io import BytesIO
from logging import getLogger
from logging.config import dictConfig

import pandas as pd
from flask import render_template, Response

from invisible_flow.app_factory import app
from invisible_flow.copa.allegation_mapper import AllegationMapper
from invisible_flow.copa.allegation_saver import AllegationSaver
from invisible_flow.copa.loader import Loader
from invisible_flow.copa.saver import Saver, strip_zeroes_from_beat_id, cast_col_to_int
from invisible_flow.globals_factory import GlobalsFactory  # noqa: F401
from invisible_flow.api.copa_scrape import scrape_data, scrape_allegation_data
from invisible_flow.copa.sorter import Sorter
from invisible_flow.transformers.allegation_transformer import AllegationTransformer
from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer

# Logging configuration

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


@app.route('/copa_scrape', methods=['GET'])
def copa_scrape():
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


@app.route('/copa_scrape_v2', methods=['GET'])
def copa_scrape_v2():
    scraped_data = scrape_allegation_data()
    scraped_df = pd.read_csv(BytesIO(scraped_data), encoding='utf-8', sep=",", dtype=str)

    crids = list(scraped_df['log_no'].values)

    allegation_mapper = AllegationMapper()
    sorter = Sorter()

    sorter.split_crids_into_new_and_old(crids, allegation_mapper.query_existing_crid_table())

    new_allegation_rows = sorter.get_new_allegation_rows(scraped_df)

    allegation_transformer = AllegationTransformer()
    transformed_new_allegation_rows = allegation_transformer.transform(new_allegation_rows)

    allegation_mapper.load_allegation_into_db(transformed_new_allegation_rows)

    # query db for data allegations associated with existing crids -- convert to df
    existing_allegation_rows = allegation_mapper.get_existing_data()

    # save new crid rows to csv
    allegation_saver = AllegationSaver()
    allegation_saver.save_allegation_to_csv(new_allegation_rows, "new_allegation_data")

    # save existing crids to csv
    allegation_saver.save_allegation_to_csv(existing_allegation_rows, "existing_allegation_data")

    # Put new crids in db
    old_crids = sorter.get_old_crids()
    new_crids = sorter.get_new_crids()

    allegation_mapper.save_new_crids_to_db(old_crids, new_crids)

    return Response(status=200, response='Success')


if __name__ == '__main__':
    app.run(debug=True)
