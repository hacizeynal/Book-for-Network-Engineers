import re
from pprint import pprint

"""
Task 15.1a
Copy the get_ip_from_cfg function from task 15.1 and redesign it so
that it returns a dictionary:
* key: interface name
* value: a tuple with two lines:
   * IP address
   * mask
Add to the dictionary only those interfaces on which IP addresses are configured.
For example (arbitrary addresses are taken):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}
To get this result, use regular expressions.
Check the operation of the function using the example of the config_r1.txt file.
Please note that in this case, you can not check the correctness
of the IP address, address ranges, and so on, since the command
output from network device is processed, not user input.
"""

result_dictionary = {}
regex = r"ip address (\S+) (\S+)"


def get_ip_from_cfg(device_config):
    with open(device_config) as k:
        for line in k:
            match_ip = re.search(regex, line)
            if line.startswith("Interface") or line.startswith("interface"):
                interface_id = line.split(" ") [ -1 ]
            elif match_ip:
                ip_address = match_ip.groups()
                result_dictionary[interface_id]=ip_address

    return result_dictionary


pprint(get_ip_from_cfg("config_r1.txt"))
