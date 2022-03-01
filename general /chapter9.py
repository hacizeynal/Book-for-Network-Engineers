# # # def check_password(username, password):
# # #     if username in password:
# # #         print("Username contains password")
# # #         return False
# # #     elif len(password) < 8:
# # #         print("Password is short ,try again")
# # #         return False
# # #
# # #     else:
# # #         print("{} has completed all tasks".format(username))
# # #         return True
# # #
# # #
# # # print(check_password('1334', 'Zeynal'))
# # #
# # #
# #
# # def sum_up(a, *args):
# #     print(a, args)
# #     return a + sum(args)
# #
# #
# # print(sum_up(5, 42, 1, 11))
# #
# #
# # def sum_arg(a, **kwargs):
# #     print(a, kwargs)
# #     return a + sum(kwargs.values())
# #
# #
# #
# # print(sum_arg(a=20,b=30))
# #
# # items = [1, 2, 3,4,5]
# #
# # print('One: {}, Two: {}, Three: {} {}'.format(*items))
#
#
# def config_interface(int_f_name, ip_address, mask):
#     interface = "{}".format(int_f_name)
#     no_shut = "no shutdown"
#     ip_address = "{} {}".format(ip_address, mask)
#     result = [ interface, no_shut, ip_address ]
#     return result
#
#
# print(config_interface('Fa0/1', '10.0.1.1', '255.255.255.0'))
#
# interfaces_info = [ [ 'Fa0/1', '10.0.1.1', '255.255.255.0' ],
#                     [ 'Fa0/2', '10.0.2.1', '255.255.255.0' ],
#                     [ 'Fa0/3', '10.0.3.1', '255.255.255.0' ],
#                     [ 'Fa0/4', '10.0.4.1', '255.255.255.0' ],
#                     [ 'Lo0', '10.0.0.1', '255.255.255.255' ] ]
#
# username_passwd = [ {'username': 'cisco', 'password': 'cisco'},
#                     {'username': 'nata', 'password': 'natapass'},
#                     {'username': 'user', 'password': '123456789'} ]
#
#
def check_password(username, password, min_length=7, check_username=True):
    if len(password) < min_length:
        print("Password is too short")
        return False
    elif check_username and username in password:
        print("Password contains username")
        return False
    else:
        print(f"Password is set for {username} and good luck !")
        return True


def add_user_to_users_file(username, users_file="user.txt"):
    while True:
        password = input("Please enter the password for {} :".format(username))
        if check_password(username, password):
            break
    with open(users_file, 'a') as f:
        f.write("\n")
        f.write("{} {}".format(username, password))


add_user_to_users_file('mamad')
