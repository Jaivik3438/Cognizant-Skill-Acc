# Task 1 - String Slicing and Indexing
# Create a string variable with the value "Python is amazing!".
# Extract the following using slicing:
# The first 6 characters ("Python")
# The word "amazing"
# The entire string in reverse order
# Print each of these slices with a clear label.

name = "Python is amazing!"

print("First word: " + name[0:6])

print("Amazing part: " + name[10:17])

print("Reverse string: " + name[::-1])