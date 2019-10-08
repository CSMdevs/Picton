import glob
import os

from PIL import Image
from resizeimage import resizeimage

def convert(img_dir):
    print("Starting conversion to jpeg for: ", img_dir)
    image_extentions = ["jpg", "png", "tiff", "gif", "webp"]
    for extention in image_extentions:
        for file in glob.glob(img_dir + "/*." + extention):
            try:
                im = Image.open(file)
                rgb_im = im.convert('RGB')
                rgb_im.save(file.replace(extention, "jpeg"), quality=70)
                os.remove(file)
                print("converted ", file, "to jpeg")
            except IOError as err:
                print(err)
                print("Continuing after error")

def downscale(img_dir):
    width = 96
    height = 96
    for file in glob.glob(img_dir + "/*.jpeg"):
        im = Image.open(file)
        im1 = im.resize((width, height), Image.ANTIALIAS)
        im1.save(file.replace("",""), quality=70)