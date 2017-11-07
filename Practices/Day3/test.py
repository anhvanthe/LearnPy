
# from openpyxl import load_workbook
# wb = load_workbook(filename = 'BomList.xlsx')
# sheet_ranges = wb['BOM1']
# #print(sheet_ranges['A18'].value)

# # for row in sheet_ranges.iter_rows(min_row=, max_col=2, max_row=):
# #     for cell in row:
# #         print(cell)

# tuple(sheet_ranges.rows)
# tuple(sheet_ranges.columns)



import http.client

conn = http.client.HTTPSConnection("api.digikey.com")

payload = "{\"SearchOptions\":[\"RoHSCompliant\"],\"Keywords\":\"TMK107BJ104KA-T\",\"RecordCount\":\"10\",\"RecordStartPosition\":\"0\",\"Filters\":{\"CategoryIds\":[27681936],\"FamilyIds\":[85103903],\"ManufacturerIds\":[86393538],\"ParametricFilters\":[{\"ParameterId\":93641443,\"ValueId\":\"311121225449472\"}]},\"Sort\":{\"Option\":\"SortByMinimumOrderQuantity\",\"Direction\":\"Descending\",\"SortParameterId\":69132357},\"RequestedQuantity\":49}"

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
    'authorization': "DsAokJNrwP0ELpoeaONMoPMX3OlK"
    }

conn.request("POST", "/services/partsearch/v2/keywordsearch", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))