import os

def rename(keyword, img_dir):
    print("Renaming downloaded files")
    counter = 1
    for filename in os.listdir(img_dir):
        ext = os.path.splitext(filename)[1]
        os.rename(img_dir + "/" + filename, img_dir + "/" + keyword + "." + str(counter).zfill(2) + ext)
        counter += 1
    print("Renamed files")