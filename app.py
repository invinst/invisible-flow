import os
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('./index.html')


@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'foia' in request.files:
        foia = request.files['foia']
        if foia.filename != '':
        	# replace with s3
        	with open('uploads/' + foia.filename, 'wb') as f:
        		f.write(foia)
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    app.run()     