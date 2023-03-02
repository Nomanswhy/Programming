value_name = input("Enter your name please: ")
print("Welcome, ", value_name)

score = input("Enter your score: ")
print("Your name is ", value_name, " and your score is ", score)

value_boolean = input("Would you like your score to be higher?")

if value_boolean == ["Yes", "yes"]:
    score += 10
    print("Your score is ", score, " now")

