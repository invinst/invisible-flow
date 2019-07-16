from flask import Flask, render_template, Response, Request

from invisible_flow.globals_factory import GlobalsFactory
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.validation import is_valid_file_type

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/foia_response_upload', methods=['POST'])
def foia_response_upload():
    request_context: Request = GlobalsFactory.get_request_context()
    storage = StorageFactory.get_storage()

    if 'multipart/form-data' not in request_context.content_type:
        return Response(status=415, response='Unsupported media type. Please upload a .csv .xls or .xlsx file.')

    foia_response_file = request_context.files['foia_response']
    if not is_valid_file_type(foia_response_file.filename):
        return Response(status=415, response='Unsupported file type. Please upload a .csv .xls or .xlsx file.')

    response_type = request_context.form['response_type']
    todays_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep="_").replace(':', '-')

    storage.store("{}.csv".format(response_type), foia_response_file, "ui-{}/initial_data".format(todays_date))

    return Response(status=200, response='Success')


if __name__ == '__main__':
    app.run()
