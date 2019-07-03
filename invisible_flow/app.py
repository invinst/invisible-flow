from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/foia_response_upload", methods=['POST'])
def foia_response_upload():
    if 'foia_response' in request.files:
        foia_response = request.files['foia_response']
        if foia_response.filename != '':
            # replace with s3
            with open('uploads/' + foia_response.filename, 'wb') as f:
                f.write(foia_response)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
