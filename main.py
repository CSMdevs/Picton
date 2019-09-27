import download
import rename

keyword = raw_input("Enter keyword: ")
count = raw_input("Enter amount of images: ")
download.download(keyword, count)
rename.rename(keyword)