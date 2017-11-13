import json
import urllib
import urllib.parse, urllib.request

url = "http://octopart.com/api/v3/parts/search"

# NOTE: Use your API key here (https://octopart.com/api/register)
url += "?apikey=1912e391" 

args = [
   ('q', 'Omron solid state relay'),
   ('start', 0),
   ('limit', 10)
   ]

url += '&' + urllib.parse.urlencode(args)

data = urllib.request.urlopen(url).read()
search_response = json.loads(data)

# print number of hits
print(search_response['hits'])

# print results
for result in search_response['results']:
   part = result['item']

   # print matched part
   print("%s - %s" % (part['brand']['name'], part['mpn']))