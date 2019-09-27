from PIL import Image
import glob
import os

for file in glob.glob("*.png"):
    im = Image.open(file)
    rgb_im = im.convert('RGB')
    rgb_im.save(file.replace("png", "jpg"), quality=70)
    os.remove(file)