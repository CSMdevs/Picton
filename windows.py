import download
import threading
import os

keywords = ["seagull", "penguin", "owl", "pigeon", "kiwi bird", "mallard", "blackbird", "sparrow", "eagle", "mallard"]

def img_actions(keyword):
    img_dir = os.path.dirname(os.path.abspath(__file__)) + "/downloads/" + keyword
    count = 1000
    download.download(keyword, count, img_dir)

for keyword in keywords:
    img_tread = threading.Thread(target = img_actions, args = (keyword, ))
    img_tread.start()

