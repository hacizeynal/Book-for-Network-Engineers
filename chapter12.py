import ipaddress
from tabulate import tabulate

ipv4 = ipaddress.ip_address("10.1.1.1")


# print(ipv4)


def check_if_ip_is_network(ip):
    try:
        ipaddress.ip_network(ip)
        return True
    except ValueError:
        return False


print(check_if_ip_is_network("10.1.1.1/24"))
print(check_if_ip_is_network("10.1.1.0/24"))

columns = [ 'Interface', 'IP', 'Status', 'Protocol' ]

sh_ip_int_br = [ ('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
                 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
                 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
                 ('Loopback0', '10.1.1.1', 'up', 'up'),
                 ('Loopback100', '100.0.0.1', 'up', 'up') ]

# print(tabulate(sh_ip_int_br))
# print(tabulate(sh_ip_int_br, headers="firstrow"))

a = [ {'IP': '15.0.15.1',
       'Interface': 'FastEthernet0/0',
       'Protocol': 'up',
       'Status': 'up'},
      {'IP': '10.0.12.1',
       'Interface': 'FastEthernet0/1',
       'Protocol': 'up',
       'Status': 'up'},
      {'IP': '10.0.13.1',
       'Interface': 'FastEthernet0/2',
       'Protocol': 'up',
       'Status': 'up'},
      {'IP': '10.1.1.1',
       'Interface': 'Loopback0',
       'Protocol': 'up',
       'Status': 'up'},
      {'IP': '100.0.0.1',
       'Interface': 'Loopback100',
       'Protocol': 'up',
       'Status': 'up'} ]

print(tabulate(a, headers="keys"))

vlanss = {"sw1": [10, 20, 30, 40], "sw2": [1, 2, 10], "sw3": [1, 2, 3, 4,5, 10, 11, 12]}

print(tabulate(vlanss,headers="keys",tablefmt="pipe",stralign="center"))



