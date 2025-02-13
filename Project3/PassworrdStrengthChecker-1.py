# Project: Password Strength Checker
# Time to Get Practical! 🔒
# In this project, you’ll create a program to check the strength of a password. The goal is to make it informative and interactive.

# Step 1: Input the Password
# Ask the user to input a password. Use the input() function for this.

# Step 2: Evaluate the Password
# Check the password for the following:

# Length: It should be at least 8 characters.
# Contain at least one uppercase letter, one lowercase letter, one digit, and one special character (like @, #, $).
# Print appropriate messages for each check:
# If it passes all checks, print: "Your password is strong! 💪"
# If it fails any check, print a message like: "Your password needs at least one digit."
# Use Python string methods like isupper(), islower(), isdigit(), and others to perform these checks.

# Step 3: Test with Different Passwords
# Here’s how the program should behave:

# Example Run 1:

# Enter a password: python123
# Your password needs at least one uppercase letter and one special character.
# Example Run 2:

# Enter a password: Python@123
# Your password is strong! 💪
# Bonus Challenge:
# Add a "password strength meter" that gives a score out of 10 based on how strong the password is.

# Make sure your program is clear, friendly, and fun to use!

import re

def check_password_strength(password):

    strength = 0
    issues = []

    if len(password) >= 8:
        strength += 2
    else:
        issues.append("at least 8 characters")

    if any(char.isupper() for char in password):
        strength += 2
    else:
        issues.append("at lease one upper character")
    
    if any(char.islower() for char in password):
        strength += 2
    else:
        issues.append("at lease one lower character")
    
    if any(char.isdigit() for char in password):
        strength += 2
    else:
        issues.append("at lease one digit")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 2
    else:
        issues.append("one special character (!@#$%^&*)")

    if strength >= 10:
        print("Your password is strong! 💪")
    else:
        print(f"Your password should have {', '.join(issues)}.")
    
    print(f"Password Strength: {strength}/10")

password = input("Enter Your Password!!")

check_password_strength(password)