import cv2
import tensorflow as tf
CATEGORIES = ["seagull", "penguin", "owl", "pigeon", "kiwi bird", "blackbird", "eagle", "mallard"]
def prepare(file):
    IMG_SIZE = 96
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def predict(image_file):
    model = tf.keras.models.load_model("CNN.model")
    image = image_file #your image path
    prediction = model.predict([prepare(image)])
    prediction = list(prediction[0])
    print(prediction)
    print(CATEGORIES[prediction.index(max(prediction))])

predict("test.jpg")
predict("test2.jpg")
predict("test3.jpg")
predict("test4.jpg")
predict("test5.jpg")
predict("test6.jpg")