# Prompt the user to enter an IP address in the format 10.0.1.1. Depending on the type of address (described below), print to the stdout:
# • ‘unicast’ - if the first byte is in the range 1-223
# • ‘multicast’ - if the first byte is in the range 224-239
# • ‘local broadcast’ - if the IP address is 255.255.255.255 • ‘unassigned’ - if the IP address is 0.0.0.0
# • ‘unused’ - in all other cases
# Restriction: All tasks must be done using the topics covered in this and previous chapters.

ip_address = input("Please enter ip address: ")
octets = ip_address.split(".")
correct_ip = True

if len(octets) != 4:
    correct_ip = False
else:
    for octet in octets:
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break
if not correct_ip:
    print("Invalid IP address")
else:
    octets_num = [int(i) for i in octets]

    if octets_num[0] in range(1, 224):
        print("This IP address is unicast")
    elif octets_num[0] in range(224, 240):
        print("This IP address is Multicast")
    elif ip_address == "255.255.255.255":
        print("This IP address is local Broadcast")
    elif ip_address == "0.0.0.0":
        print("This IP address is Unassigned")
    else:
        print("This IP address is Unused")

