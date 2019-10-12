import os
import shutil
from flask import Flask, request, render_template, url_for, redirect
import look

app = Flask(__name__)
predict_dir = os.path.dirname(os.path.abspath(__file__)) + "/predict/"
@app.route("/")
def fileFrontPage():
    return render_template('fileform.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        for files in os.listdir(predict_dir):
            file_path = os.path.join(predict_dir, files)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)    
        photo = request.files['photo']
        if photo.filename != '':            
            photo.save(os.path.join(predict_dir,photo.filename))
            look.webpredict()
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    app.run()     