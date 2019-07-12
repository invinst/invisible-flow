from flask import Flask, request, render_template, Response

from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.validation import is_valid_file_type

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/foia_response_upload', methods=['POST'])
def foia_response_upload():
    storage = StorageFactory.get_storage()
    foia_response_file = request.files['file']

    if 'multipart/form-data' not in request.content_type:
        return Response(status=415, response='Unsupported media type. Please upload a .csv .xls or .xlsx file.')

    if not is_valid_file_type(foia_response_file.filename):
        return Response(status=415, response='Unsupported file type. Please upload a .csv .xls or .xlsx file.')

    storage.store(foia_response_file.filename, foia_response_file)

    return Response(status=200, response='Success')


if __name__ == '__main__':
    app.run()
