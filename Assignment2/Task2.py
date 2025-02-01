# Task 2 - Multiplication Table with for Loops

number = int(input("Enter a number for that you want to print Table:"))

for i in range(1,11):
    answer = number * i
    print(f"{number:2} * {i:2} : {answer:2}")
