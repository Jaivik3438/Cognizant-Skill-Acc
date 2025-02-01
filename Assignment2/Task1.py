# Task 1 - Counting Down with Loops
startingNumber = int(input("Enter count down staring number!!"))

if startingNumber > 0:
    while startingNumber > 0:
        print(startingNumber, end=" ")
        startingNumber -= 1
    print("Blast off! 🚀")
else:
    print("Please enter integer formate of number!")