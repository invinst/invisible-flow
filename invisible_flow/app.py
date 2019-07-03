from flask import Flask, request, render_template, Response

from invisible_flow.constants import FOIA_RESPONSE_UPLOAD_DIR, FOIA_RESPONSE_FIELD_NAME

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/foia_response_upload", methods=['POST'])
def foia_response_upload():
    foia_response_file = request.files.get('file')
    if 'multipart/form-data' in request.content_type and FOIA_RESPONSE_FIELD_NAME in foia_response_file.filename:
        if foia_response_file.filename != '':
            # We may not need to write the file to the local disk if we can upload directly to the cloud.
            with open('{}{}'.format(FOIA_RESPONSE_UPLOAD_DIR, FOIA_RESPONSE_FIELD_NAME), 'wb') as file:
                file.write(foia_response_file.read())
                file.close()
    return Response(status=200, response='Success')


if __name__ == '__main__':
    app.run()
