import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "http://py4e-data.dr-chuck.net/comments_973515.json"
data = urllib.request.urlopen(address).read().decode()
info = json.loads(data)

num = 0
for item in info['comments']:
    num += int(item['count'])
print('Sum:' + str(num))
    