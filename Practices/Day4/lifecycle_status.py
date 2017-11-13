import json
import urllib

queries = [
    {'mpn': 'SN74S74N',
     'reference': 'line1'},
    {'sku': '67K1122',
     'reference': 'line2'},
    {'mpn_or_sku': 'SN74S74N',
     'reference': 'line3'},
    {'brand': 'Texas Instruments',
     'mpn': 'SN74S74N',
     'reference': 'line4'}
    ]

url = 'http://octopart.com/api/v3/parts/match?queries=%s' \
    % urllib.quote(json.dumps(queries))
url += "&include[]=specs"

# NOTE: Use your API key here (https://octopart.com/api/register)
url += '&apikey=REPLACE_ME'

data = urllib.urlopen(url).read()
response = json.loads(data)

# print request time (in milliseconds)
print "Response time: %s msec\n" % response['msec']

# print mpn's
for result in response['results']:
    print "Reference: %s" % result['reference']
    for item in result['items']:
        # get lifecycle status
        if 'lifecycle_status' in item['specs']:
            lifecycle_status = item['specs']['lifecycle_status']['value'][0]
        else:
            lifecycle_status = 'Unknown'

        brand_name = item['brand']['name']
        mpn = item['mpn']
        print "\t%s %s: %s" % (brand_name, mpn, lifecycle_status)
