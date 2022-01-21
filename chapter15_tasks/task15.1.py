"""
Create a get_ip_from_cfg function that expects the name of the file containing the device configuration as an argument.

The function should process the configuration and return the IP addresses and masks that are configured on the
interfaces as a list of tuples:

the first element of the tuple is the IP address
the second element of the tuple is a mask
For example (arbitrary addresses are taken):

[("10.0.1.1", "255.255.255.0"), ("10.0.2.1", "255.255.255.0")]
To get this result, use regular expressions.

Check the operation of the function using the config_r1.txt file.

Please note that in this case, you can not check the correctness of the IP address, address ranges, and so on,
since the command output from network device is processed, not user input.

"""
import re
from pprint import pprint

# result = [ ]
# regex = r"ip address (\S+) (\S+)"
#
#
# def get_ip_from_cfg(device_config):
#     with open(device_config) as f:
#         for line in f:
#             match_ip = re.search(regex, line)
#             if match_ip:
#                 result.append(match_ip.groups())
#     return result
#
#
# pprint(get_ip_from_cfg("config_r1.txt"))

# second version
result = [ ]


# def get_ip_from_cfg(device_config):
#     regex = r"ip address (\S+) (\S+)"
#     with open(device_config) as k:
#         for i in re.finditer(regex, k.read()):
#             result.append(i.groups())
#     return result
#
#
# pprint(get_ip_from_cfg("config_r1.txt"))

# third version

def get_ip_from_cfg(device_config):
    regex = r"ip address (\S+) (\S+)"
    with open(device_config) as k:
        result_list = [ j.groups() for j in re.finditer(regex, k.read()) ]
    return result_list


pprint(get_ip_from_cfg("config_r1.txt"))
