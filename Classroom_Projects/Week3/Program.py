MENU = "1) Login \n2) Quit"

# MENU is constant, that's why its in a caps

print(MENU)
valid_username = "Oleh"
valid_password = "4679"

user_choice = input("Choose options [1/2] > ")

while 1:
    if user_choice == "1":
        enter_username = input("Enter your username > ")
        if enter_username == valid_username:
            enter_password = input("Enter your password > ")
        else:
            print("Invalid username!")
            continue_ask = input("Would you like to continue? > \n")
            if continue_ask == "yes" or continue_ask == "Yes":
                continue
            else:
                print("Quitting...")
                break
        if enter_password == valid_password:
            print("Logging you in...")
            break
        else:
            print("Invalid password!")
            continue_ask = input("Would you like to continue? > \n")
            if continue_ask == "yes" or continue_ask == "Yes":
                continue
            else:
                print("Quitting...")
                break
    else:
        print("Quitting...")
        break
