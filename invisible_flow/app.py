from logging import getLogger
from logging.config import dictConfig

from flask import render_template, Response, Request

from invisible_flow.app_factory import app
from invisible_flow.copa.loader import Loader
from invisible_flow.copa.saver import Saver, strip_zeroes_from_beat_id, cast_col_to_int
from invisible_flow.globals_factory import GlobalsFactory
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.transformers.transformer_factory import TransformerFactory
from invisible_flow.validation import is_valid_file_type
from invisible_flow.api.copa_scrape import scrape_data
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


@app.route('/foia_response_upload', methods=['POST'])
def foia_response_upload():
    request_context: Request = GlobalsFactory.get_request_context()

    try:
        foia_response_file = request_context.files['foia_response']
    except Exception as e:
        logger.error(e)
        return Response(status=400, response="No file with name foia_response was uploaded")

    if not is_valid_file_type(foia_response_file.filename):
        logger.error(f'Unsupported file type uploaded to FOIA. filename={foia_response_file.filename}')
        return Response(status=415, response='Unsupported file type. Please upload a .csv .xls or .xlsx file.')

    try:
        response_type = request_context.form['response_type']
    except Exception as e:
        logger.error(e)
        return Response(status=400, response="No response type for the file was specified")

    logger.info(f'Received foia request of type {response_type}')

    current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')

    file_content: bytes = foia_response_file.read()

    logger.info(f'Storing foia request of type {response_type}')
    storage = StorageFactory.get_storage()
    storage.store_byte_string(f'{response_type}.csv', file_content, f'ui-{current_date}/initial_data')

    logger.info(f'Transforming foia request of type {response_type}')
    transformer = TransformerFactory.get_transformer(response_type)
    transformation_result = transformer.transform(response_type, file_content.decode('utf-8'))
    logger.info(f'Storing transformed file')
    for result in transformation_result:
        storage.store_byte_string(f'{result[0]}.csv', result[1].encode('utf-8'), f'ui-{current_date}/transformed')

    logger.info('Successfully uploaded FOIA file')
    return Response(status=200, response='Success')


if __name__ == '__main__':
    app.run(debug=True)

