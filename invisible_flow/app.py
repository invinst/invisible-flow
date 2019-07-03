from flask import Flask, request, render_template, Response

from invisible_flow.constants import FOIA_RESPONSE_UPLOAD_DIR, FOIA_RESPONSE_FIELD_NAME
from invisible_flow.validation import is_valid_file_type

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/foia_response_upload', methods=['POST'])
def foia_response_upload():
    foia_response_file = request.files['file']

    if 'multipart/form-data' not in request.content_type:
        return Response(status=415, response='Unsupported media type. Please upload a .csv por and .xlsx file.')

    if not is_valid_file_type(foia_response_file.filename):
        return Response(status=415, response='Unsupported file type. Please upload a .csv por and .xlsx file.')

    # We may not need to write the file to the local disk if we can upload directly to the cloud.
    with open('{}{}'.format(FOIA_RESPONSE_UPLOAD_DIR, FOIA_RESPONSE_FIELD_NAME), 'wb') as file:
        file.write(foia_response_file.read())
        file.close()
    return Response(status=200, response='Success')


if __name__ == '__main__':
    app.run()
