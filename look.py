import cv2
import tensorflow as tf
import glob
import logging

CATEGORIES = ["seagull", "penguin", "owl", "pigeon", "kiwi bird", "blackbird", "eagle", "mallard"]

def prepare(file):
    IMG_SIZE = 96
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def predict(image_file):
    model = tf.keras.models.load_model("datasets/CNN.model")
    image = image_file
    prediction = model.predict([prepare(image)])
    prediction = list(prediction[0])

    predicted_cat = CATEGORIES[prediction.index(max(prediction))]
    predicted_crt = str(prediction[prediction.index(max(prediction))]*100) + "%"

    return predicted_cat, predicted_crt
