# Task 3 - Find the Factorial

number = int(input("Enter a number to find factorial! "))
factorial = 1

if number > 0:
    for item in range(1,number+1):
        factorial = factorial * item

    print(f"Factorial of {number} is: {factorial}")
else:
    print("Factorial can not be find for negative number or zero!!")

