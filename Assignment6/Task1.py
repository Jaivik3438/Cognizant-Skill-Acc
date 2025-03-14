def divide_100_by_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            result = 100 / num
            print(f"100 divided by {num} is {result}.")
            break
        except ZeroDivisionError:
            print("Oops! You cannot divide by zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    divide_100_by_number()