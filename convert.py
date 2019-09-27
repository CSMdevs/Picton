from PIL import Image
import glob
import os
from resizeimage import resizeimage


def convert(img_dir):
    width = 96
    height = 96

    print("")
    print("Starting conversion to jpg:")
    
    for file in glob.glob(img_dir + "/*.png"):
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        rgb_im.save(file.replace("png", "jpg"), quality=70)
        print("Converted " + file + " to jpg")
        os.remove(file)
        
    for file in glob.glob(img_dir + "/*.jpeg"):
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        rgb_im.save(file.replace("jpeg", "jpg"), quality=70)
        print("Converted " + file + " to jpg")
        os.remove(file)
        
    for file in glob.glob(img_dir + "/*.tiff"):
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        rgb_im.save(file.replace("tiff", "jpg"), quality=70)
        print("Converted " + file + " to jpg")
        os.remove(file)


def downscale(img_dir):
    for file in glob.glob(img_dir + "/*.jpg"):
        im = Image.open(file)
        im1 = im.resize((width, height), Image.ANTIALIAS)
        im1.save(file.replace("",""), quality=70)