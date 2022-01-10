# access_template = [ 'switchport mode access', 'switchport access vlan', 'spanning-tree portfast',
#                     'spanning-tree ''bpduguard enable' ]
# #
# # commands = [' switchport mode access', ' spanning-tree portfast', ' spanning-tree bpduguard enable\n']
# #
# # fast_interface = ["0/1","0/2","0/3","0/9","0/10"]
# #
# # for each in fast_interface:
# #     print("interface {}".format(each))
# # #     for command in commands:
# # #         print(command)
# # #
# # #
# #
# #
# # fast_int = {'access': {'0/12': 10, '0/14': 11, '0/16': 17, '0/17': 150}}
# #
# # same_dic = fast_int [ "access" ]
# # print(same_dic)
# #
# # for interface_id, vlan in same_dic.items():
# #     print("interface FastEthernet" + interface_id)
# #     for add_commands in access_template:
# #         if add_commands.endswith("access vlan"):
# #             print(" {} {}".format(add_commands, vlan))
# #         else:
# #             print(" {}".format(add_commands))
# #
# # # Comments to the code:
# # # • The first for loop iterates keys and values in nested fast_int[‘access’] dictionary • At this moment of loop the current key is stored in intf variable
# # # • At this moment of loop the current value is stored in vlan variable
# # # • String “interface Fastethernet” is displayed with interface number added
# # # • The second loop for iterates commands from access_template list
# # # • Since switchport access to vlan command requires a VLAN number:
# # # – within second loop for commands are checked – if command ends with “access vlan”
# # # ∗ command is displayed and VLAN number is added to it – in all other cases, command is simply displayed
# #
# #
# # b = 5
# #
# # while b > 0:
# #     print(b)
# #     b = b - 1
#
#
# username = input('Enter username: ')
# password = input('Enter password: ')
#
# check_password = False
#
# while not check_password:
#     if len(password) < 8:
#         print('Password is too short\n')
#         password = input('Enter password once again: ')
#     elif username in password:
#         print('Password contains username\n')
#         password = input('Enter password once again: ' )
#     else:
#         print('Password for user {} is set'.format(username))
#         check_password = True
#

var = False
if not var:
    print('learnt stuff')
