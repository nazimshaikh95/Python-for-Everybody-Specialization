import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL : ')
print('Retrieving ', url)
html = urllib.request.urlopen(url)
charlen = html.read().decode()
content = ""
for line in html:
    content = content + (line.decode().strip())

stuff = ET.fromstring(content)
lst = stuff.findall('comments/comment')
print('Count:', len(lst))
print('Retrieved Characters:',len(charlen))
sum = 0
for item in lst:
    sum = sum + int(item.find('count').text)
print('Sum:',sum)
