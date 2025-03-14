import turtle

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def draw_fractal(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal(branch_length - 15, t)
        t.left(40)
        draw_fractal(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Please enter a positive integer.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\nWelcome to the Recursive Artistry Program!")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        match choice:
            case "1":
                num = get_positive_integer("Enter a number to find its factorial: ")
                print(f"The factorial of {num} is {factorial(num)}.")
            
            case "2":
                num = get_positive_integer("Enter the position of the Fibonacci number: ")
                print(f"The {num}th Fibonacci number is {fibonacci(num)}.")
            
            case "3":
                screen = turtle.Screen()
                screen.bgcolor("white")
                t = turtle.Turtle()
                t.speed(0)
                t.left(90)
                t.up()
                t.backward(100)
                t.down()
                draw_fractal(100, t)
                screen.mainloop()
            
            case "4":
                print("Thank you for using the Recursive Artistry Program! Goodbye!")
                break
            
            case _:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
