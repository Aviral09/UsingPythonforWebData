address = 'http://py4e-data.dr-chuck.net/comments_973514.xml'
if len(address) < 1: break

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
# print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
# print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('.//count')
for result in results:
    sum+=result.find('count').text
print(sum)