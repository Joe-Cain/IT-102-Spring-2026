'''
Password checker for strength based on length and complexity
'''

#Libraries used for this script:
import re
import sys

#list of commonly used passwords
COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein", "Password01", "qwerty", "abc123", 
    "welcome", "1234567890", "password!", "pa$$w0rd"
]

def check_password_strength(password):
    '''
    Checks password strength and returns feedback and score
    +1 for length of >= 8
    +2 for length of >= 12
    +1 for upper and lower case
    +1 for digit
    +1 for special character
    Deductions:
    -2 if password is in common password list
    '''

    score = 0
    feedback = []

    #check min length
    if len(password) >= 8:
        score +=1
    else:
        feedback.append("Your password is too short. 8 characters minimum required")

    #check regular length
    if len(password) >= 12:
        score += 1
        feedback.append("Good length of 12+ characters")
    else:
        feedback.append("Please consider using 12+ characters to be more secure")

    #check case
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
        feedback.append("Contains both upper and lower case")
    else:
        feedback.append("Please mix upper and lower case")

    #check for digit
    if re.search(r'\d', password):
        score += 1
        feedback.append("Contains at least one digit or number")
    else:
        feedback.append("Adding a number is recommended")

    #check special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>_\-]', password):
        score += 1
        feedback.append("Contains at least one special character")
    else:
        feedback.append("Adding a special character is recommended")

    #check password list
    if password.lower()in COMMON_PASSWORDS:
        score -=2
        feedback.append("This is a common password, and easily guessed")

    #determine password strength
    score = max(score, 0)
    if score <= 1:
        strength = "Very weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very strong"

    return score, strength, feedback

    #main
def main():
    print("Password Strength Checker")

    #Accept password from command line
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Please enter your password to check: ")

    score, strength, feedback = check_password_strength(password)

    print(f" Score: {score}")
    print(f" Strength: {strength}")
    print("\n Feedback:")

    for line in feedback:
        print(f" {line}")

#call main
if __name__ == "__main__":
    main()