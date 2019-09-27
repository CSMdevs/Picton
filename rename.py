import os

def rename(keyword):
    img_dir = os.path.dirname(os.path.abspath(__file__)) + "/downloads/" + keyword
    counter = 1
    for filename in os.listdir(img_dir):
        print(img_dir + "/" + filename)
        ext = os.path.splitext(filename)[1]
        os.rename(img_dir + "/" + filename, img_dir + "/" + str(counter) + ext)
        counter += 1
