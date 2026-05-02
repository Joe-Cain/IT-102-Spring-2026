#!/usr/bin/env python3
# Sample script that reads from a file
# By Joe Cain
"""
This is to read the file I created from the script writefile.py
"""
#create a loop to open file and read its contents
with open("hackme.txt", "r") as file:
    contents = file.read()
    print("Here is someone to hack - info dump")
    print(contents)
