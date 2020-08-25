import random
import urllib.request

def download(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

download("https://images.unsplash.com/photo-1573417946005-21a8db578c32?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=933&q=80")
