import os

from google_images_download import google_images_download


def download(keyword, count):
    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": keyword,
        "limit": count,
        "print_urls": False,
        "output_directory": os.path.dirname(os.path.abspath(__file__)) + "/downloads/"
    }
    paths = response.download(arguments)
