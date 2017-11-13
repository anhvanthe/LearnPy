# Section 1
# Convert csv file into line items and queries
# This code assumes a file format similar to the one on the
# Arduino BOM
import csv


csv_file = open("arduino_bom.csv", "r")
csv_reader = csv.DictReader(csv_file)
line_items = []
queries = []
for line_item in csv_reader:
    # Skip line items without part numbers and manufacturers
    if not line_item['Part Number'] or not line_item['Manufacturer']:
        continue
    line_items.append(line_item)
    queries.append({'mpn': line_item['Part Number'],
                    'brand': line_item['Manufacturer'],
                    'reference': len(line_items) - 1})