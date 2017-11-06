
import urllib.request
import urllib.parse

# # x = urllib.request.urlopen(url)
# # print(x.read())

# data = urllib.parse.urlencode(keywordsearch)
# data = data.encode('utf-8') # data should be bytes
# req = urllib.request.Request(url2, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()

# print(respData)


import http.client

conn = http.client.HTTPSConnection("api.digikey.com")

payload = "{\"SearchOptions\":[\"RoHSCompliant\"],\"Keywords\":\"p5555-nd\",\"RecordCount\":\"10\",\"RecordStartPosition\":\"0\",\"Filters\":{\"CategoryIds\":[27681936],\"FamilyIds\":[85103903],\"ManufacturerIds\":[86393538],\"ParametricFilters\":[{\"ParameterId\":93641443,\"ValueId\":\"311121225449472\"}]},\"Sort\":{\"Option\":\"SortByMinimumOrderQuantity\",\"Direction\":\"Descending\",\"SortParameterId\":69132357},\"RequestedQuantity\":49}"

headers = {
    'x-ibm-client-id': "85ab7852-8280-42c8-8a9c-2302c1cb029f",
    'content-type': "application/json",
    'accept': "application/json",
    'x-digikey-locale-site': "US",
    'x-digikey-locale-language': "en",
    'x-digikey-locale-currency': "USD",
    'x-digikey-locale-shiptocountry': "US",
    'x-digikey-customer-id': "tuongpv",
    'x-digikey-partner-id': "tuongpv",
    'authorization': "0AllrTCvjfeAHVHjtwot7KjltL30"
    }

conn.request("POST", "/services/partsearch/v2/keywordsearch", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

