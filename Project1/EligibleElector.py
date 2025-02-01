# Project: Eligible Elector
# asked user age 
age = int(input("How old are you? 🎉"))

# checked age of user for eligibility
if age > 0:
    if age >= 18:
        print("Congratulations!  🎉 You are eligible to vote. Go make a difference!")
    else:
        # calculated remaining years to be eligible for vote
        yearsLeft = 18 - age
        print(f"Oops! You’re not eligible yet. 😅 But hey, only {yearsLeft} more years to go! 🎂")
else:
    print(f"Ohh, it seems you are not born yet! 🤔 Stay inside and enjoy the ride! 🍼")