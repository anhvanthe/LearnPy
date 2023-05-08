import os
from os import listdir
from os.path import isfile, join

mypath = "c:\\tool"
logpath = "c:\\Tool\\JEE\\HW\\HW-ASPICE"
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)
# print('\n')

# arr = os.listdir()
# print(arr)

print("Start scan.........................plz wait.........")

mylog = open("mylog.txt", "a", encoding="utf-8")

thisdir = mypath #os.getcwd()

# r=root, d=directories, f = files

# for r, d, f in os.walk(thisdir):
#     for file in f:
#         if file.endswith(".docx"):
#             print(os.path.join(r, file))

for path, subdirs, files in os.walk(thisdir):
    for name in files:
        mylog.write(os.path.join(path, name))
        mylog.write('\n')
        print("..")
    	#print(subdirs)
    	#if name.endswith(".docx"):
        #	print(os.path.join(path, name))

mylog.close()

print("Done...........Bye Bye--------------------------------")