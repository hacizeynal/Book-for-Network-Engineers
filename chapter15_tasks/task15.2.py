"""
Task 15.2
Create a function parse_sh_ip_int_br that expects as an argument the name
of the file containing the output of the show ip int br command.
The function should process the output of the show ip int br command
and return the following fields:
* Interface
* IP-Address
* Status
* Protocol
The information should be returned as a list of tuples:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]
To get this result, use regular expressions.
Check the operation of the function using the example of the sh_ip_int_br.txt file.

"""
import re
from pprint import pprint
zeynal_list = [ ]


def parse_sh_ip_int_br(interface_details):
    with open(interface_details) as k:
        match_regex = re.finditer("(?P<interface>\S+)\s+(?P<address>\S+)\s+\w+\s+\w+\s+("
                                  "?P<status>up|administratively down)\s+(?P<protocol>up|down)", k.read())
        for i in match_regex:
            zeynal_list.append(i.groups())
    return zeynal_list


pprint(parse_sh_ip_int_br("show_ip_int_br.txt"))
