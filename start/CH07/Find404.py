#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Joe Cain

#Print any IP that has a 404 status

'''
This script is designed to return 404 source ip
'''

#libraries used
import re

def main():
    LOG_FILE = r"C:\Users\justincase\Desktop\IT.102\IT-102-Spring-2026\start\CH07\access.log"
    with open(LOG_FILE, "r") as f:
        for line in f:
            #status code immediately following request and first numbers
            ip = line.split()[0]
            match = re.search(r'" 404 ', line)
            if match:
                print(f"{ip}")
    

if __name__ == "__main__":
    main()