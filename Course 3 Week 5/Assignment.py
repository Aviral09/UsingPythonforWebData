import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "http://py4e-data.dr-chuck.net/comments_973514.xml"
uh = urllib.request.urlopen(address)
data = uh.read()
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
num = 0 
for result in results:
    num += int(result.find('count').text)
print('Count: ' + str(len(results))) 
print('Sum:' + str(num))
    