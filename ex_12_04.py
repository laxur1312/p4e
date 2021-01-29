#Este ejercicio extrae el conteo de tags de párrafo

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count=0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

try:
    html = urllib.request.urlopen(url, context=ctx).read()
except:
    print('Invalid URL')
    exit()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    #print((tag.text).strip())
    count=count+1

print(count)
