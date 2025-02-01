# Project: Number Guessing Game
import random

number_to_guess = random.randint(1, 100)
print("**************************************************************")
print("🎲 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")
print("You have 10 attempts. Good luck!")
print("**************************************************************")
print()

attempts = 0
max_attempts = 10

while attempts < max_attempts:
        user_entered_number = int(input("Enter a number between 1 to 100:-"))
        attempts += 1
        if user_entered_number > 0 and user_entered_number <= 100:
            if number_to_guess > user_entered_number:
                print(f"{user_entered_number} Too low! Try again.")
                
            elif number_to_guess < user_entered_number:
                print(f"{user_entered_number} Too high! Try again.")

            else:
                print(f"{user_entered_number} Congratulations! You guessed it in {attempts} attempts!") 
                break 
        else:
             print("Please follow a rule of game and enter number between 1 to 100, Don't be too smart!!")
else:
    print("Game over! Better luck next time!")
           


