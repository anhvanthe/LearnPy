import can
import csv

filename = "Logging2022-09-16_09-48-14.blf"
log = can.BLFReader(filename)
log = list(log)

log_output = []

for msg in log:
    msg = str(msg)
    log_output.append([msg[18:26],msg[38:40],msg[40:42],msg[46],msg[62],msg[67:90]])

with open("output.csv", "w", newline='') as f:
    writer = csv.writer(f,delimiter=';', quotechar='\"', quoting=csv.QUOTE_ALL)
    writer.writerows(log_output)
