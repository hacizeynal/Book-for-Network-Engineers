import re
from pprint import pprint


def parse_cdp(filename):
    result = {}

    with open(filename) as file:
        for each_line in file:
            if each_line.startswith("Device ID"):
                neighbor = re.search('Device ID: (\S+)', each_line).group(1)
                result [ neighbor ] = {}
            elif each_line.startswith("  IP address"):
                ip = re.search('IP address: (\S+)', each_line).group(1)
                result [ neighbor ] [ 'ip' ] = ip
            elif each_line.startswith("Platform"):
                platform = re.search("Platform: (\S+ \S+),", each_line).group(1)
                result [ neighbor ] [ "platform" ] = platform
            elif each_line.startswith("Cisco IOS Software"):
                ios = re.search("Cisco IOS Software, (.+)", each_line).group(1)
                result [ neighbor ] [ "software version" ] = ios
    return result


pprint(parse_cdp("cdp_neighbors.txt"))
