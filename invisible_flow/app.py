import os

from flask import Flask, request, render_template, Response
from google.cloud import storage

from invisible_flow.Storage.IStorage import IStorage
from invisible_flow.Storage.LocalStorage import LocalStorage
from invisible_flow.constants import FOIA_RESPONSE_FIELD_NAME
from invisible_flow.validation import is_valid_file_type

app = Flask(__name__)

if (os.environ.get('ENVIRONMENT_PROFILE') == 'local'):
    storageI = LocalStorage()
else:
    storageI = IStorage()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/foia_response_upload', methods=['POST'])
def foia_response_upload():
    foia_response_file = request.files['file']
    print(foia_response_file)

    if 'multipart/form-data' not in request.content_type:
        return Response(status=415, response='Unsupported media type. Please upload a .csv .xls or .xlsx file.')

    if not is_valid_file_type(foia_response_file.filename):
        return Response(status=415, response='Unsupported file type. Please upload a .csv .xls or .xlsx file.')

    # gcs_client = storage.Client()
    # bucket = gcs_client.bucket(os.environ.get('GCS_BUCKET'))
    # blob = bucket.blob(FOIA_RESPONSE_FIELD_NAME)
    # blob.upload_from_string(foia_response_file.stream.read(), foia_response_file.content_type)

    return Response(status=200, response='Success')




if __name__ == '__main__':
    app.run()
