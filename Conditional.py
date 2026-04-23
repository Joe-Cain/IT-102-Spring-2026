'''Create a conditional that takes an input and if it's a yes, returns a reply.
'''

#This is going to take an input from the user
answer = input("Is today a good day? (Y/N)" ).lower()

#if statement to check if the answer is y, if it is, print yes it is
if answer == "y":
    print("Yes it is!")
