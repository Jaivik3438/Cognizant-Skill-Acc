# Task 4 - Understanding Recursion
# Write a recursive function factorial to calculate the factorial of a number.
# Then, write another recursive function fibonacci to calculate the nth number in the Fibonacci sequence.

# Example Output:

# plaintext
# Copy code
# Factorial of 5 is 120. The 6th Fibonacci number is 8.

def factorial(n):
    if n==1: 
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
a = 1
b = 1
number = 5
n = 8
answer = factorial(number)
print(f"Factorial of {number} is {answer}.", end=" ")
print(f"The Fibonacci of {n}th number is {fibonacci(n)}")
