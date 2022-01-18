import re

# text = ''' Extract the doamin from the urls www.gcptutorials.com,
# www.wikipedia.org, www.google.com'''
#
# pattern = r'(www.([A-Za-z_0-9-]+)(.\w+))'
#
#
# find_iter_result = re.finditer(pattern, text)
#
# print(type(find_iter_result))
# print(find_iter_result)
#
# for i in find_iter_result:
#     print(i.group(2))
#
import re
from pprint import pprint

result = [ ]
regex = "ip address (\S+) (\S+)"


def get_ip_from_cfg(device_config):
    with open(device_config) as f:
        for line in f:
            if match_ip:
                result.append(match_ip.groups())
    return result


pprint(get_ip_from_cfg("config_r1.txt"))

# result = [ m.groups() for m in re.finditer(regex, f.read()) ]
