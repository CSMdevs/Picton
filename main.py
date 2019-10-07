import download
import rename
import convert
import os


keyword = raw_input("Enter keyword: ")
img_dir = os.path.dirname(os.path.abspath(__file__)) + "/downloads/" + keyword
count = raw_input("Enter amount of images: ")
download.download(keyword, count, img_dir)
rename.rename(keyword, img_dir)
convert.convert(img_dir)
convert.downscale(img_dir)

