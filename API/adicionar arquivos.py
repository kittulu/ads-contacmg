import os
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename
from application import App

app = App.app()
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 160 * 1000 * 1000
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        
        if 'file' not in request.files:
            return ('No file part')
            #return redirect(request.url)
        file = request.files['file']

  
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('download_file', name=filename))
            return 'deu certo'
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''