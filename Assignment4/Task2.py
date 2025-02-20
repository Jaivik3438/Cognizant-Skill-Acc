# Task 2 - Exploring Dictionaries

# Create a dictionary to store information about yourself with the following keys: "name", "age", "city".
# Add a new key-value pair to the dictionary for "favorite color".
# Update the "city" key with a new value.
# Print all the keys and values using a loop.

personalInformaion = {
    "name":"Tony Stark",
    "age":61,
    "city":"New York",
}

print(personalInformaion)

personalInformaion["favorite color"] = "Red"

print(personalInformaion)

personalInformaion["city"] = "Taxes"

print(personalInformaion)

print(f"Keys: ", end=" ")
for key in personalInformaion: 
    print(key + ",", end=", ") 

print()

print(f"Values: ", end=" ")
for values in personalInformaion.values(): 
    print(values , end=", ") 