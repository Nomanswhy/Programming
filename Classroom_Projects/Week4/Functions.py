def function(x):
    return x * 5


variable = 5


# print(function(variable))

def ask():
    age = int(input("What is your age? > "))
    if age > 17:
        print("Congrats, you are not underage")
    else:
        print("Oh no, you are underage")


# ask()

def factorial_recursion(input1):
    if input1 == 1 or input1 == 0:
        return 1
    elif input1 < 0:
        return print("Error, input is less than 0")
    else:
        return input1 * factorial_recursion(input1 - 1)


parameter = int(input("Input a number factorial of which you want to get > "))

print(factorial_recursion(parameter))
