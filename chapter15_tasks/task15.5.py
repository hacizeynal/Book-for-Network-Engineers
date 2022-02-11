"""
Task 15.5
Create a generate_description_from_cdp function that expects as an argument
the name of the file that contains the output of the show cdp neighbors command.
The function should process the show cdp neighbors command output and generate
a description for the interfaces based on the command output.
For example, if R1 has the following command output:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1
For the Eth 0/0 interface, you need to generate the following description:
description Connected to SW1 port Eth 0/1
The function must return a dictionary, in which the keys are the names
of the interfaces, and the values are the command specifying the description
of the interface:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'
Check the operation of the function on the sh_cdp_n_sw1.txt file.
"""

import re
from pprint import pprint

full_regex = re.compile(
    "(?P<remote_device>\w+) +(?P<local_interface>\S+ \S+) +\d+ +[\w ]+  +\S+ +(?P<remote_interface>\S+ \S+)")

final_config = """description Connected to {remote_device} port {remote_interface}"""

final_dictionary = {}


def generate_description_from_cdp(config_file):
    with open(config_file) as raw_data:
        catch = full_regex.finditer(raw_data.read())
        for i in catch:
            k = i.groupdict()
            # print(k)
            # create Dictionary based on exact matched patterns ,keys will be group names such as (remote_device,
            # local_interface and etc)
            final_dictionary [ i.group(2) ] = final_config.format(**k) # Dictionary unpacking
    return final_dictionary


pprint(generate_description_from_cdp("show_cdp.txt"))
