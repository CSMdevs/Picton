import download
import rename
import convert
import os
import threading


#keyword = raw_input("Enter keyword: ")
keywords = ["seagull", "penguin", "owl", "pigeon", "kiwi bird", "mallard", "blackbird", "sparrow", "eagle", "mallard"]

def img_actions(keyword):
    img_dir = os.path.dirname(os.path.abspath(__file__)) + "/downloads/" + keyword
    count = 100
    download.download(keyword, count, img_dir)
    rename.rename(keyword, img_dir)
    convert.convert(img_dir)
    convert.downscale(img_dir)

for keyword in keywords:
    img_tread = threading.Thread(target = img_actions, args = (keyword, ))
    img_tread.start()

