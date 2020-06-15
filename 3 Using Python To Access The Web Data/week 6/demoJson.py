import json
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
content = ""
for line in html:
    content = content + (line.decode().strip())
js = json.loads(content)

sum = 0
counter = 0
for i in js["comments"]:
    counter = counter + 1
    sum = sum + int(i["count"])

print('Count:', counter)
print('Retrieved Characters:',len(content))
print('Sum:',sum)
