from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Larissa.html"

for i in range (0,7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    target = 18
    count = 0
    tags = soup('a')
    for tag in tags:
        count +=1
        if count == 18:
            url = tag.get('href', None)
            break

print(url[(int(url.find('by_')))+3:int(url.find('.html'))])
