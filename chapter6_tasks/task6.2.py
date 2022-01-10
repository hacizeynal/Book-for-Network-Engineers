# Prompt the user to enter an IP address in the format 10.0.1.1. Depending on the type of address (described below), print to the stdout:
# • ‘unicast’ - if the first byte is in the range 1-223
# • ‘multicast’ - if the first byte is in the range 224-239
# • ‘local broadcast’ - if the IP address is 255.255.255.255 • ‘unassigned’ - if the IP address is 0.0.0.0
# • ‘unused’ - in all other cases
# Restriction: All tasks must be done using the topics covered in this and previous chapters.

ip = input("Please enter an IP address to check : ")
first_octet = int(ip.split(".")[0])


if 1 <= first_octet <= 223:
    print("This is unicast IP address ")
elif 224 <= first_octet <= 239:
    print("This is multicast IP address ")
elif ip == '255.255.255.255':
    print("This address is broadcast IP address")
elif ip == "0.0.0.0":
    print("This ip is unassigned IP address")
else:
    print("This IP address is unused")









