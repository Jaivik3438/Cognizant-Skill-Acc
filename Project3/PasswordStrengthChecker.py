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

password = input("Enter your Password!!")

uppercase_checkpoint = False
lowercase_checkpoint = False
specialCharacter_checkpoint = False
digit_checkpoint = False


if len(password) < 8:
    print("Password should have at least 8 characters")
else:
   for char in password:
        if char.isupper():
           uppercase_checkpoint = True
        elif char.islower():
            lowercase_checkpoint = True
        elif char.isdigit():
            digit_checkpoint = True
        else:
            specialCharacter_checkpoint = True

if uppercase_checkpoint == True & lowercase_checkpoint == True & digit_checkpoint == True & specialCharacter_checkpoint == True:
     print("Your password is strong! 💪")
else:
    if uppercase_checkpoint == False:
        print("Your password needs at least one uppercase letter")

    if lowercase_checkpoint == False:
        print("Your password needs at least one lowercase letter")

    if digit_checkpoint == False:
        print("Your password needs at least one digital letter")   

    if specialCharacter_checkpoint == False:
        print("Your password needs at least one Special character")
