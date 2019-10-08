import os
import shutil
from google_images_download import google_images_download


def download(keyword, count, img_dir):
    if os.path.exists(img_dir):
        shutil.rmtree(img_dir)
    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": keyword,
        "limit": count,
        "print_urls": False,
        "output_directory": os.path.dirname(os.path.abspath(__file__)) + "/downloads/",
        "chromedriver": os.path.dirname(os.path.abspath(__file__)) + "/chromedriver.exe",
        "silent_mode": False
    }
    paths = response.download(arguments)
