ip = input("Enter IP address: \n")
octets = ip.split(".")
print(octets)
valid_ip = len(octets) == 4

for i in octets:
    valid_ip = i.isdigit() and 0 <= int(i) <= 255

if valid_ip:
    if 1 <= int(octets[0]) <= 223:
        print("unicast")
    elif 224 <= int(octets[0]) <= 239:
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")
else:
    print("Invalid IP address")

