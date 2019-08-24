from logging import getLogger
from logging.config import dictConfig

from flask import render_template, Response, Request

from invisible_flow.app_factory import app
from invisible_flow.globals_factory import GlobalsFactory
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.transformers.transformer_factory import TransformerFactory
from invisible_flow.validation import is_valid_file_type

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


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


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

    file_content: str = foia_response_file.read().decode('utf-8')

    logger.info(f'Storing foia request of type {response_type}')
    storage = StorageFactory.get_storage()
    storage.store_string(f'{response_type}.csv', file_content, f'ui-{current_date}/initial_data')

    logger.info(f'Transforming foia request of type {response_type}')
    transformer = TransformerFactory.get_transformer(response_type)
    transformation_result = transformer.transform(response_type, file_content)
    logger.info(f'Storing transformed file')
    for result in transformation_result:
        storage.store_string(f'{result[0]}.csv', result[1], f'ui-{current_date}/transformed')

    logger.info('Successfully uploaded FOIA file')
    return Response(status=200, response='Success')


if __name__ == '__main__':
    app.run()
