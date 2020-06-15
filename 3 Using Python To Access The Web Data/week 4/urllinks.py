# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL : ')
count  = int(input('Enter count : '))
pos = int(input('Enter position : '))

# Retrieve all of the anchor tags
while count != 0 :
    print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    counter = 0 
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))
        url = tag.get('href', None)
        if counter == pos-1 :
            break
        counter = counter + 1
    count = count - 1
####################################################
str1 = url.split('/')                               #extracting name from last retrived URL
str2 = str1[3].split('_')
str3 = str2[2].split('.')
print(str3[0])                                      # printing name of last retrieved URL
