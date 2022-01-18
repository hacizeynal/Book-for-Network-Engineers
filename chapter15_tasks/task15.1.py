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

result = [ ]


def get_ip_from_cfg(device_config):
    regex = (r"ip address (\w+\.\w+\.\w+\.\w) (\d+\.\d+\.\d+\.\d+)")
    with open(device_config) as f:
        for line in f:
            print(line)
            match_ip = re.match(regex, line)
            if match_ip:
                result.append(match_ip.groups())
    return result


print(get_ip_from_cfg("config_r1.txt"))
