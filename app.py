import os
import shutil
from flask import Flask, request, render_template, url_for, redirect
from waitress import serve
import hashlib
import look
import logging
import json
import base64
import pathlib


app = Flask(__name__)

app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
predict_dir = os.path.dirname(os.path.abspath(__file__)) + "/predict/"

def allowed_image(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


@app.route("/")
def home():
    return render_template('fileform.html')

@app.route("/result")
def result():
    result = json.loads(request.args['result'])

    try:
        img_path = os.path.join(predict_dir, result["filename"])
        with open(img_path, "rb") as photo:
            photo_string = base64.encodestring(photo.read()).decode('utf-8')
            photo_type = pathlib.Path(result["filename"]).suffix

            image = {
                "src": photo_string,
                "type": photo_type
            }

        os.remove(img_path)
        
        
    except FileNotFoundError:
        image = {
            "src": "",
            "type": ""
        }

    return render_template('result.html', result=result, image=image)

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']

        if photo.filename == '':
            return redirect(url_for('home'))
        
        if allowed_image(photo.filename) == False:
            return redirect(url_for('home'))

        photo.filename = str(0) + '.' + photo.filename

        photo_location = os.path.join(predict_dir, photo.filename)

        photo.save(photo_location)

        prediction, certainty = look.predict(photo_location)

        result = {
            "prediction": prediction,
            "certainty": certainty,
            "filename": photo.filename
        }
        return redirect(url_for("result", result=json.dumps(result)))
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(threaded=True, port=5000)    