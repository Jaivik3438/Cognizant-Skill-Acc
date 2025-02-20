# Task 1 - Writing Functions
# Create a function greet_user that accepts a name as a parameter and prints a personalized greeting.
# Then, write another function add_numbers that takes two numbers as parameters, adds them, and returns the result.

# Example Output:

# plaintext
# Copy code
# Hello, Alice! Welcome aboard. The sum of 5 and 10 is 15.

def greet_user(name):
    print(f"Hello {name}!! Welcom aboard.", end= " ")

def add_numbers(a,b):
    return a+b

greet_user("Tony Stark")
a = 25
b = 10
sum = add_numbers(a,b)
print(f"The sum of {a} and {b} is {sum}.")