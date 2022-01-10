def check_password(username, password, min_length=7, check_username=True):
    if len(password) < min_length:
        print("Password is too short")
        return False
    elif check_username and username in password:
        print("Password contains username")
        return False
    else:
        print(f"Password is set for {username} and good luck !")  # or we could return the string
        return True  # we have to return True manually to break loop in add_user_to_users_file() function


def add_user_to_users_file(username, users_file="user.txt"):
    while True:
        password = input("Please enter the password for {} :".format(username))
        if check_password(username, password):
            # write to the file if there check_password() returns True
            with open(users_file, 'a') as f:
                f.write("{} {}".format(username, password))
            break


add_user_to_users_file('Zeynal')  # this we do not need to print
