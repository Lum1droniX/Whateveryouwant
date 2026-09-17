# Hayden Fillmore

    # This project is meant to recreate a simple password creation system.
    # It requires a minimum of 12 characters and a mix of uppercase/lowercase characters.
    # It will not be allowed to contain spaces, as well as special characters and numbers cause I couldn't figure it out.
    # The rule about not using the same password is invalid since the passwords won't be stored.
    # The forum I found "getpass" from: https://stackoverflow.com/questions/9202224/getting-a-hidden-password-input
    # Kind of hard committed and realized hiding the password is redundant without hidden unput :P

import getpass

# ==========

print("================================")
print("")
print("The following code was made to recreate a password creator:")

# ==========

while True:
    print("")
    NewPassword = getpass.getpass("What would you like your new password to be? ")
    print("")
    if " " in NewPassword:
        print("---Password cannot contain spaces---")
    elif NewPassword == NewPassword.lower():
        print("---Password needs at least one uppercase letter---")
    elif NewPassword == NewPassword.upper():
        print("---Password needs at least one lowercase letter---")
    elif len(NewPassword) < 12:
        print("---Password needs at least 12 characters---")
    else:
        print("================================")
        print("")
        print(f"Password: {"*" * len(NewPassword)}")
        break

# ==========

while True:
    ShowPass = input("Would you like to show the password (Yes/No)? ").upper()
    print("")
    if ShowPass == "YES":
        print(f'Password: {NewPassword}')
        HidePass = input("Would you like to hide the password (Yes/No)? ").upper()
        if HidePass == "YES":
            print("")
            print(f'Password: {"*" * len(NewPassword)}')
        elif HidePass == "NO":
            print("")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f'Your new password is "{NewPassword}"!')
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            break
        else:
            print("Invalid input")
    elif ShowPass == "NO":
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Your new password has been saved!")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        break
    else:
        print("Invalid input")



