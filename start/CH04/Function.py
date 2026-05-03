#!/usr/bin/env python3
# Sample script "function"
# By Joe Cain
'''
Create a conditional that takes an input and if affirmative returns a reply
'''
#This is going to receive input from the user
answer = input("Is today a good day? (y/n) ").lower()

'''
Loops yes it is if the response is = yes
'''
def send_message():
      for x in range(10):
            print("Yeah it is!")
#An if statement checking if the string is equal to y and if so print yes it is
if answer == "y":
    send_message()
elif answer == "n":
    print("Im sorry")
else:
          print("Please try again")