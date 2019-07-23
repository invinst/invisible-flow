from logging import getLogger
from logging.config import dictConfig

from flask import Flask, render_template, Response, Request

from invisible_flow.globals_factory import GlobalsFactory
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.validation import is_valid_file_type
from invisible_flow.transformers.transformer_factory import TransformerFactory

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

app = Flask(__name__)

logger = getLogger(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/foia_response_upload', methods=['POST'])
def foia_response_upload():
    request_context: Request = GlobalsFactory.get_request_context()

    if 'multipart/form-data' not in request_context.content_type:
        logger.error('Unsupported media type uploaded to FOIA. content type={}'.format(request_context.content_type))
        return Response(status=415, response='Unsupported media type. Please upload a .csv .xls or .xlsx file.')

    foia_response_file = request_context.files['foia_response']
    if not is_valid_file_type(foia_response_file.filename):
        logger.error('Unsupported file type uploaded to FOIA. filename={}'.format(foia_response_file.filename))
        return Response(status=415, response='Unsupported file type. Please upload a .csv .xls or .xlsx file.')

    storage = StorageFactory.get_storage()
    response_type = request_context.form['response_type']
    current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')

    file_content = foia_response_file.read()

    storage.store_string('{}.csv'.format(response_type), file_content, 'ui-{}/initial_data'.format(current_date))

    transformer_factory = TransformerFactory.get_transformer(response_type)
    transformer_factory.transform(response_type, file_content)
    allegations = TransformerFactory.get_transformer(response_type).transform(response_type, file_content)
    storage.store_string('{}.csv'.format(response_type), allegations, 'ui-{}/transformed'.format(current_date))

    logger.info('Successfully uploaded FOIA file')
    return Response(status=200, response='Success')


if __name__ == '__main__':
    app.run()
