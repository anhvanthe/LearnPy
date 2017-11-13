import json
import urllib

url = "http://octopart.com/api/v3/parts/search"

# NOTE: Use your API key here (https://octopart.com/api/register)
url += "?apikey=REPLACE_ME" 

args = [
   ('q', 'solid state relay'),
   ('start', 20),
   ('limit', 20)
   ]

url += '&' + urllib.urlencode(args)

data = urllib.urlopen(url).read()
search_response = json.loads(data)

# print number of hits
print search_response['hits']

# print results
for result in search_response['results']:
   part = result['item']

   # print matched part
   print "%s - %s" % (part['brand']['name'], part['mpn'])
