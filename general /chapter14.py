# """
#
# Regular expression syntax
#
# \d - any digit
# \D - any non-numeric value
# \s - whitespace character
# \S - all except whitespace characters
# \w - any letter, digit or underline character
# \W - all except letter, digit or underline character
#
# """
#
import re

#
# int_line = '  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
#
# match = re.search('BW \d+', int_line)
# # print(match)
#
#
# log2 = 'Oct  3 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF: Host f04d.a206.7fd6 in vlan 1 is flapping between port Gi0/5 ' \
#        'and port Gi0/16 '
#
# x = re.search('Host (\S+) in vlan (\d+) is flapping between port (\S+) and port (\S+)', log2).groups()
# # y = re.search('\d\d:\d\d:\d\d', log).group()
#
# # print(x)
#
# log1 = '*Jul  7 06:15:18.695: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down'
# pattern1 = re.search('\d\d:\d\d:\d\d', log1).group()
# pattern2 = re.search('\d+', log1).group()
# import re
#
# log2 = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.bc16.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
# pattern3 = re.search("\w\w\w\w.\w\w\w\w.\w\w\w\w", log2).group()
# pattern4 = re.search("\w\w\w\w\.\w\w\w\w.\w\w\w\w", log2).group()
# # print(pattern3)
# # print(pattern4)
#
# email1 = 'user1@gmail.com'
# email2 = 'user2.test@gmail.com'
#
# pattern6 = re.search("", email1).group()
# pattern7 = re.search("", email2).group()
# # print(pattern6)
# # print(pattern7)
#
# mac_table = '''
#  sw1#sh mac address-table
#             Mac Address Table
#  -------------------------------------------
#
#  Vlan    Mac Address       Type        Ports
#   ----    -----------       --------    -----
# 100    a1b2.ac10.7000    DYNAMIC     Gi0/1
# 200    a0d4.cb20.7000    DYNAMIC     Gi0/2
# 300    acb4.cd30.7000    DYNAMIC     Gi0/3
# 1100    a2bb.ec40.7000    DYNAMIC     Gi0/4
# 500    aa4b.c550.7000    DYNAMIC     Gi0/5
# 1200    a1bb.1c60.7000    DYNAMIC     Gi0/6
# 1300    aa0b.cc70.7000    DYNAMIC     Gi0/7
#
# '''
#
# for line in mac_table.split("\n"):
#     matchj = re.search("\d{1,4} +", line)
#     if matchj:
#         print("vlan id is ", matchj.group())
#
# cdp = '''
# SW1#show cdp neighbors detail
# -------------------------
# Device ID: SW2
# Entry address(es):
# IP address: 10.1.1.2
# Interface: GigabitEthernet1/0/11,  Port ID (outgoing port): GigabitEthernet0/2
# Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP
# Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1
# Holdtime : 164 sec
#
# '''
#
# # cdp_match = re.search("Interface. .+Port ID.+",cdp).group()
# print(cdp_match)

# commands = [ 'SW1#show cdp neighbors detail','SW1>sh ip int br','r1-london-core# sh ip route' ]
#
# for line in commands:
#     match = re.search("^.+[#>]",line)
#     if match:
#         print(match.group())

regex = re.compile("(?P<mac_address>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<interfac_name_ide>\S+)")
result = []

with open("dhcp_snooping.txt") as dhcp_data:
    for line in dhcp_data:
        match = regex.search(line)
        if match:
            result.append(match.groupdict())

print(f'{len(result)} devices connected to switch')

for number ,comp in enumerate(result,1):
    print(f'Parameters of device {number}:')
    for key in comp:
        print(f'{key:10} : {comp[key]:10}')


