# Task 2 - Using Default Parameters
# Create a function describe_pet that accepts two parameters:

# pet_name (string)
# animal_type (string, default value is "dog").
# The function should print a description of the pet.

# Example Output:

# plaintext
# Copy code
# I have a dog named Buddy. I have a cat named Whiskers.

def describe_pet(pet_name, animal_type = "dog"):
    print(f"I have a {animal_type} named {pet_name}.", end=" ") 


describe_pet("tomy")
describe_pet("rome","cat")