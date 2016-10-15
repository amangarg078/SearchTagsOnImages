import requests
from py_bing_search import PyBingImageSearch
import os

os.chdir('./static/images')

def downloadImages():
    bing_image = PyBingImageSearch('Enter your Bing Search app id here ', "live concert")
    images = bing_image.search(limit=50, format='json')
    for i in range(len(images)):
        req_get_image=requests.get(images[i].media_url)
        f=open(str(i)+".jpg","wb")
        f.write(req_get_image.content)
        f.close()

for j in range(40):
    downloadImages()
