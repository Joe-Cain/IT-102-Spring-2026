#!/usr/bin/env python3
# example workign with Loops
#By Joe Cain
'''Create a loop and a conditional that takes an input and if it's a yes, 
print 10 times when a reply is given.
'''

#This is going to take an input from the user
answer = input("Is today a good day? (Y/N)" ).lower()

#if statement to check if the answer is y, if it is, print yeah it is
if answer == "y":
    for _ in range(10):
        print("Yeah it is")
