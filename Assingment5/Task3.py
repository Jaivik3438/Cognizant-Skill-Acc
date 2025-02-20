# Task 3 - Functions with Variable Arguments
# Write a function make_sandwich that accepts a variable number of arguments for sandwich ingredients and prints them as a list.

# Example Output:

# plaintext
# Copy code
# Making a sandwich with the following ingredients: - Lettuce - Tomato - Cheese

def make_sandwich(*args):
    print("Making a sandwich with the following ingredients: ", end =" ")
    for item in args:
        print(f"- {item}", end =" ")

make_sandwich("Lettuce","Tomato","Cheese","Bread")