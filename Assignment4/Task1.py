# Task 1 - Working with Lists

# Create a list of your favorite fruits. Add at least five fruits to the list.
# Perform the following operations:
# Append a new fruit to the list.
# Remove one fruit from the list using the remove() method.
# Print the list in reverse order using slicing.

fruits = ["Apple", "Banana", "Orange", "Berry", "Elderberry", "Date"]

print(f"Original list: {fruits}")

fruits.append("Fig")

print(f"After adding a fruit: {fruits}")

fruits.remove("Apple")

print(f"After removing a fruit: {fruits}")

print(f"After removing a fruit: {fruits[:: -1 ]}")