ip = input("Enter IP Address: ")
ipv4 = ip.split('.')
if 1 <= int(ipv4 [ 0 ]) <= 223:
    status = "Unicast"
elif 224 <= int(ipv4 [ 0 ]) <= 239:
    status = "Multicast"
elif (int(ipv4 [ 0 ])) and (int(ipv4 [ 1 ])) and (int(ipv4 [ 2 ])) and (int(ipv4 [ 3 ])) == 255:
    status = "Broadcast"
elif int(ipv4 [ 1 ]) == 0 and int(ipv4 [ 2 ]) == 0 and int(ipv4 [ 3 ]) == 0 and int(ipv4 [ 0 ]) == 0:
    status = "Unassigned"
else:
    status = "Unused"
print(status)

# ip = input("Enter IP Address: ")
# ipv4 = ip.split('.')
# print(ipv4)
# if 1 <= int(ipv4[0]) <= 223:
#     status = "Unicast"
# elif 224 <= int(ipv4[0]) <= 239:
#     status = "Multicast"
# elif ((int(ipv4[0])) and (int(ipv4[1])) and (int(ipv4[2])) and (int(ipv4[3]))) == 255:
#     status = "Broadcast"
# elif ((int(ipv4[0])) and (int(ipv4[1])) and (int(ipv4[2])) and (int(ipv4[3]))) == 0:
#     status = "Unassigned"
# else:
#     status = "Unused"
# print(status)
