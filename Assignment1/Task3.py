# Task 3 - Conditional Statements: The Number Checker

# Ask the user to enter a number
user_input = input("Please enter a number: ")

# Convert the input to an integer
num = int(user_input)

# Print the number entered by the user
print(f"User entered the number: {num}")

# Conditions to check numbers
if num > 0:
    print(f"This {num} number is positive. Awesome!")
elif num < 0:
     print(f"This {num} number is negative. Better luck next time!")
else:
     print("Zero it is. A perfect balance!")