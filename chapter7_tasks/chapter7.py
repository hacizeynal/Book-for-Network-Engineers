# result = {}
#
# with open("show_ip_int_br.txt") as k:
#     for line in k:
#         line = line.split()
#         if line and line[1][0].isdigit():
#             interface, address, *other = line
#             result[interface] = address
#
# print(result)

# result2 = {}
# with open("show_interface.txt") as l:
#     for line in l:
#         if "line protocol" in line:
#             interface = line.split() [ 0 ]
#         elif "MTU" in line:
#             mtu = line.split() [ -8 ]
#             result2[interface] = mtu
#
# print(result2)

# result3 = {}
#
# with open("show_interface.txt") as m:
#     for line in m:
#         if "line protocol" in line:
#             interface = line.split()[0]
#             result3[interface] = {}
#             # print(result3)
#         elif "Internet address" in line:
#             ip_address = line.split()[-1]
#             result3[interface]['ip'] = ip_address
#         elif "MTU" in line:
#             mtu = line.split()[2]
#             result3[interface]['mtu'] = mtu
# print(result3)

# result4 = {}
# 
# with open("show_interface2.txt") as u:
#     for line in u:
#         if "line protocol" in line:
#             interface = line.split()[0]
#         elif "Internet address" in line:
#             ip_address = line.split()[-1]
#             result4[interface]= {}
#             result4[interface]["ip"] = ip_address
#         elif "MTU" in line:
#             mtu = line.split()[2]
#             result4[interface]['mtu'] = mtu
#
# print(result4)

x = [1, 2, 3]
y = [4, 5, 6]

x.append(y)
print(x)