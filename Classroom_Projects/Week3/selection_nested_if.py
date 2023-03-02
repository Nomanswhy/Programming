result = int(input("Enter student's result > "))

"""
if result >= 50:
    if result == 50:
        print("Well-done!")
    else:
        print("Excellent Job!")
else:
    print("Unfortunately you didn't pass:(")
"""

if result < 0:
    print("Invalid result")
elif result <= 59:
    print("Unfortunately you didn't pass:(")
elif (result >= 60) and (result <= 69):
    print("You got a D mark")
elif (result >= 70) and (result <= 79):
    print("You got a C mark")
elif (result >= 80) and (result <= 89):
    print("You got a B mark!")
elif (result >= 90) and (result <= 99):
    print("You got an A mark!")
elif result == 100:
    print("Congratulations, you got a highest mark!!!")
else:
    print("Invalid result!")
