# Project: Implement Your own Data Structures
# Let's Get Real! 🛒
# In this project, you’ll create a simple inventory management program dictio using lists,naries, and tuples.

# Step 1: Create the Inventory

# Start with an empty dictionary called inventory.
# Each key in the dictionary will represent an item name, and the value will be a tuple containing the quantity and price.
# Example:

# inventory =
# {
# "apple": (10, 2.5),
# "banana": (20, 1.2)
# }
# Step 2: Add, Remove, and Update Items

# Add functionality to:
# Add a new item to the inventory (e.g., "mango": (15, 3.0)).
# Remove an item from the inventory.
# Update the quantity or price of an existing item.
# Step 3: Display the Inventory
# Write a loop to display all items in the inventory in a friendly format. For example:

# Item: apple, Quantity: 10, Price: $2.5
# Item: banana, Quantity: 20, Price: $1.2

# Step 4: Bonus - Calculate Total Value
# Add a feature to calculate and display the total value of the inventory by multiplying the quantity and price of each item.

# Example Run:

# Welcome to the Inventory Manager!
# Current inventory:
# Item: apple, Quantity: 10, Price: $2.5
# Item: banana, Quantity: 20, Price: $1.2
# Adding a new item: mango
# Updated inventory:
# Item: apple, Quantity: 10, Price: $2.5
# Item: banana, Quantity: 20, Price: $1.2
# Item: mango, Quantity: 15, Price: $3.0
# Total value of inventory: $90.0
# Make sure your program is interactive, user-friendly, and easy to use. Add comments to explain your code for bonus clarity!

inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

print(f"Current Inventory: {inventory}")
# inventory.items() use to iterate over key and value at the same time
for key,(quantity,pricePerItem) in inventory.items():
    print(f"Item: {key} Quantity: {quantity} Price: {pricePerItem}") 

newItem = input("Enter new inventory Item: ")
quantity = int(input("Enter quantity of newly added Item: "))
pricePerItem = float(input("Enter price one newly added Item: "))
inventory[newItem] = (quantity, pricePerItem)

for key,(quantity,pricePerItem) in inventory.items():
    print(f"Item: {key} Quantity: {quantity} Price: {pricePerItem}") 

print(f"Updated Inventory: {inventory}")

totalOfInventory = 0

# Calculation of total value of Inventorys
for key,(quantity,pricePerItem) in inventory.items():
    print(f"Item: {key} Quantity: {quantity} Price: {pricePerItem}")  
    totalInventoryPerFruit = quantity * pricePerItem
    totalOfInventory += totalInventoryPerFruit

print(f"Total value of inventory:: {totalOfInventory}")
