# Task 3 - Check for Palindromes
# Write a Python program to check if a string is a palindrome (reads the same backward and forward).

# Ask the user to input a word.
# Use slicing to reverse the string and compare it with the original.
# Print a friendly message indicating whether the word is a palindrome.
# Example Run:

# Enter a word: madam
# Yes, 'madam' is a palindrome!

name = input("Enter a string!! ")

print(f"Entered string is {name}")

reversed_string = name[::-1]

print(f"Reversed String is {reversed_string}")

if name == reversed_string:
    print(f"Yes, {name} is a palindrome!")
else:
    print(f"No, {name} is not palindrome!")