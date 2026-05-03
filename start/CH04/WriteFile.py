#!/usr/bin/env python3
# Sample script that writes to a file
# By Joe Cain
# Script 1 - Collect info and save to hackme.txt
"""
Write a script that saves user input into a file that gathers data about the user
"""

#These variables are questions that need answers
name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What was the name of your first pet? ")
maiden = input("What is your mother's maiden name? ")
school = input("What elementary school did you attend? ")
with open("hackme.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Favorite color: {color}\n")
    file.write(f"First pet: {pet}\n")
    file.write(f"Mother's maiden name: {maiden}\n")
    file.write(f"Elementary school: {school}\n")

    print("Saved to hackme.txt Great work!")
