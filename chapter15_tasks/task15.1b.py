"""
Task 15.1b
Check the get_ip_from_cfg function from task 15.1a on the config_r2.txt configuration.
Note that there are two IP addresses assigned on the e0/1 interface:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary
And in the dictionary returned by the get_ip_from_cfg function, only one of them
(first or second) corresponds to the Ethernet0/1 interface.
Copy the get_ip_from_cfg function from 15.1a and redesign it to return
a list of tuples for each interface in the dictionary value.
If only one address is assigned on the interface, there will be one tuple in the list.
If several IP addresses are configured on the interface, then the list will
contain several tuples. The interface name remains the key.
Check the function in the config_r2.txt configuration and make sure the
Ethernet0/1 interface matches a list of two tuples.
Please note that in this case, you can not check the correctness
of the IP address, address ranges, and so on, since the command
output from network device is processed, not user input.
"""

import re
from pprint import pprint

result_dict = {}


def get_ip_from_cfg(config_device):
    with open(config_device) as f:
        regex_match = re.finditer("interface (\S+)\n"
                                  "(?: .*\n)*"
                                  " ip address \S+ \S+\n"
                                  "( ip address \S+ \S+ secondary\n)*",
                                  f.read())
        # print(type(regex_match))
        # print(regex_match)
        for i in regex_match:
            # print(i.group())
            # print(type(i.group()))
            result_dict [ i.group(1) ] = re.findall("ip address (\S+) (\S+)", i.group())
    return result_dict


pprint(get_ip_from_cfg("config_r2.txt"))
