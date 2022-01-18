import re

log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 ' \
      'and port Gi0/15 '
log2 = '%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24'

match = re.search('Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)', log)
match2 = re.search('Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)', log2)

# print(match2)
# print(match2.groups())
#
# regex = ('Host \S+ '
#          'in vlan (\d+) '
#          'is flapping between port '
#          '(\S+) and port (\S+)')
#
# ports = set()
#
# with open("log.txt") as f:
#     for line in f:
#         match3 = re.search(regex, line)
#         if match3:
#             vlan = match3.group(1)
#             ports.add(match3.group(2))
#             ports.add(match3.group(3))
#
# print(" Loop between ports {} {}".format(" ,".join(ports), vlan))
#

sh_ip_int_br = '''
R1#show ip interface brief
Interface             IP-Address      OK? Method Status           Protocol
FastEthernet0/0       15.0.15.1       YES manual up               up
FastEthernet0/1       10.0.12.1       YES manual up               up
FastEthernet0/2       10.0.13.1       YES manual up               up
FastEthernet0/3       unassigned      YES unset  up               up
Loopback0             10.1.1.1        YES manual up               up
Loopback100           100.0.0.1       YES manual up               up
'''

groups = [ ]

result = re.finditer(r'(\S+) +'
                     r'([\d.]+) +'
                     r'\w+ +\w+ +'
                     r'(up|down|administratively down) +'
                     r'(up|down)', sh_ip_int_br)

for mat in result:
    groups.append(mat.groups())

print(groups)

mac_address_table = open("show_mac_address.txt").read()

