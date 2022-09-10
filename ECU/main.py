from asyncio.windows_events import NULL
import os
import string
import time
import csv
import sys

from operator import length_hint
from sys import flags
from os import listdir

list_files = listdir(".\\data")

print("VF8 LOG INTERPRETER")
print("Created by TuongPV4")
print("Please wait...........................")
print("......................................")


SW_VER_KEY = "ReadDataByIdentifier:response DID data: 62 f1 88:  "
SW_REV_KEY = "ReadDataByIdentifier:response DID data: 62 f1 48:  "
HW_VER_KEY = "ReadDataByIdentifier:response DID data: 62 f1 91:  "
HW_REV_KEY = "ReadDataByIdentifier:response DID data: 62 f1 41:  "
HW_VER_KEY2 = "['22', 'f1', '91']"
NEW_KEY = "INFO:UdsClient:response DID data: "

DID_KEY = "INFO:UdsClient:ReadDataByIdentifier<0x22> - Reading data identifier : "

# Searching for "Start of ECU log"
def start_of_ecu_log(file_name):
    KEY_WORD = "INFO:__main__:ECU"
    counter = 0
    OLD_ECU_name = ""
    ECU_name = ""
    SW_ver = ""
    SW_rev = ""
    HW_ver = ""
    HW_rev = ""
    DID = ""

    #ecu_flags = False
    hw_flag = False
    sw_flag = False
    hw_rev_flag = False
    sw_rev_flag = False

    with open(file_name, "r") as log_file:
        while True:
            line_content = log_file.readline()
            if line_content:
                if ("INFO:__main__:ECU name:" in line_content):
                    ECU_name = line_content.strip().split(": ")[1]
                    if ECU_name != OLD_ECU_name:
                        OLD_ECU_name = ECU_name
                        print("-------------------------------------------------")
                        print(OLD_ECU_name)
                        # ecu_flags = True
                        hw_flag = False
                        sw_flag = False
                        hw_rev_flag = False
                        sw_rev_flag = False
                elif (DID_KEY in line_content):
                    DID = line_content.strip().split(DID_KEY)[1][2:6]


                elif (SW_VER_KEY in line_content) and (sw_flag == False) :
                    SW_ver = line_content.strip().split(SW_VER_KEY)[1]
                    print("SW Version: " + SW_ver)
                    sw_flag = True

                elif (SW_REV_KEY in line_content) and (sw_rev_flag == False) :
                    SW_rev = line_content.strip().split(SW_REV_KEY)[1]
                    print("SW Rev    : " + SW_rev)
                    sw_rev_flag = True

                elif (HW_VER_KEY in line_content) and (hw_flag == False):
                    HW_ver = line_content.strip().split(HW_VER_KEY)[1]
                    print("HW Version: " + HW_ver)
                    hw_flag = True
                    
                elif (HW_REV_KEY in line_content) and (hw_rev_flag == False) :
                    HW_rev = line_content.strip().split(HW_REV_KEY)[1]
                    print("HW Rev    : " + HW_rev)
                    hw_rev_flag = True

                elif (NEW_KEY in line_content):
                    if DID == "f188":
                        if (line_content.strip().split(NEW_KEY)[1] != NULL):
                            print("SW Version: " + line_content.strip().split(NEW_KEY)[1])

                    if DID == "f191":
                        if (line_content.strip().split(NEW_KEY)[1] != NULL):
                            print("HW Version: " + line_content.strip().split(NEW_KEY)[1])
           
            else:
                break

    log_file.close()
    return counter

############ TEST ###########

if __name__ == "__main__":
    for file_log in list_files:
        full_file_name = ".//data//" + file_log
        print("Parsing file " + file_log)
        start_of_ecu_log(full_file_name)
