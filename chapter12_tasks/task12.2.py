"""
Task 12.2
The ping_ip_addresses function from task 12.1 only accepts a list of addresses,
but it would be convenient to be able to specify addresses using a range,
for example 192.168.100.1-10.
In this task, you need to create a function convert_ranges_to_ip_list that
converts a list of IP addresses in different formats into a list where each
IP address is listed separately.
The function expects as an argument a list containing IP addresses
and/or ranges of IP addresses.
List items can be in the format:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10
If the address is specified as a range, the range must be expanded into
individual addresses, including the last address in the range.
To simplify the task, we can assume that only the last octet of the
address changes in the range.
The function returns a list of IP addresses.
For example, if you pass the following list to the convert_ranges_to_ip_list function:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
The function should return a list like this:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']
"""
import ipaddress

list_containing_ips_with_range = [ '8.8.4.4', '11.111.1.21-31', '172.20.41.128-172.21.41.132', "192.168.0.1-3" ]

list_containing_full_ips = [ ]


def check_valid_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def convert_ranges_to_ip_list(hosts):
    for each_ip in hosts:
        if check_valid_ip_address(each_ip):
            list_containing_full_ips.append(each_ip)
        elif "-" in each_ip:
            first_ip = each_ip.split("-") [ 0 ]
            first_ip_except_last_octet = first_ip.split(".") [ 0:3 ]
            first_ip_except_last_octet = ".".join(first_ip_except_last_octet)
            # print(first_ip_except_last_octet)
            last_ip = each_ip.split("-") [ -1 ]
            if not check_valid_ip_address(last_ip):
                last_octet = each_ip.split(".") [ -1 ].split("-")
                first_index = int(last_octet [ 0 ])
                last_index = int(last_octet [ -1 ])
                for k in range(first_index, last_index + 1):
                    final_ip = first_ip_except_last_octet + "." + str(k)
                    list_containing_full_ips.append(final_ip)
            elif check_valid_ip_address(last_ip):
                a = int(first_ip.split(".") [ -1 ])
                b = int(last_ip.split(".") [ -1 ])
                for c in range(a, b + 1):
                    final_ip = first_ip_except_last_octet + "." + str(c)
                    list_containing_full_ips.append(final_ip)

    return list_containing_full_ips


print(convert_ranges_to_ip_list(list_containing_ips_with_range))

#    Second method ##


# import ipaddress
#
# lisaa = [ "1.1.1.2-9", "172.30.30.31-172.30.31.34" ]
#
#
# def convert_ranges_to_ip_list(ip_addresses):
#     ip_list = [ ]
#     for ip_address in ip_addresses:
#         if "-" in ip_address:
#             start_ip, stop_ip = ip_address.split("-")
#             if "." not in stop_ip:
#                 stop_ip = ".".join(start_ip.split(".") [ :-1 ] + [ stop_ip ])
#             start_ip = ipaddress.ip_address(start_ip)
#             stop_ip = ipaddress.ip_address(stop_ip)
#             for ip in range(int(start_ip), int(stop_ip) + 1):
#                 ip_list.append(str(ipaddress.ip_address(ip)))
#         else:
#             ip_list.append(str(ip_address))
#     return ip_list
#
#
# print(convert_ranges_to_ip_list(lisaa))
