"""
Task 17.3
Create a function parse_sh_cdp_neighbors that processes the output of
the show cdp neighbors command.
The function expects, as an argument, the output of the command
as a single string (not a filename).
The function should return a dictionary that describes the connections between devices.
For example, if the following output was passed as an argument:
R4>show cdp neighbors
Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
The function should return a dictionary like this:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}
Interfaces must be written with a space. That is, so Fa 0/0, and not so Fa0/0.
Check the function on the contents of the sh_cdp_n_sw1.txt file
"""
import re
from pprint import pprint

regex_match = re.compile(
    r"(?P<remote_device>\w+)  +(?P<local_interface>\S+ \S+)"
    r"  +\d+  +[\w ]+  +\S+ +(?P<remote_interface>\S+ \S+)"
)

hostname_regex = re.compile(r"(?P<hostname>\S+)>show cdp neighbors")
final_dictionary = {}


def parse_sh_cdp_neighbors(cdp_neighbor_txt):
    with open(cdp_neighbor_txt) as k:
        for line in k:
            hostname_match = hostname_regex.match(line)
            details_match = regex_match.search(line)
            if hostname_match:
                hostname = hostname_match.group("hostname")
                final_dictionary [ hostname ] = {}
            elif details_match:
                remote_device = details_match.group("remote_device")
                local_interface = details_match.group("local_interface")
                remote_interface = details_match.group("remote_interface")
                final_dictionary [ hostname ] [ local_interface ] = {remote_device: remote_interface}
        return final_dictionary


if __name__ == "__main__":
    pprint(parse_sh_cdp_neighbors("sh_cdp_sw1.txt"))
