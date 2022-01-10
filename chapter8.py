# topology = [ [ 'sw1', 'Gi0/1', 'r1', 'Gi0/2' ],
#              [ 'sw1', 'Gi0/2', 'r2', 'Gi0/1' ],
#              [ 'sw1', 'Gi0/3', 'r3', 'Gi0/0' ],
#              [ 'sw1', 'Gi0/5', 'sw4', 'Gi0/2' ] ]
#
# width = 20
# for connection in topology:
#     l_device, l_port, r_device, r_port = connection
#     # print("{} {} {} {}".format(l_device, l_port, r_device, r_port))
#     print(f"{l_device:{width}}{l_port:{width}}{r_port:{width}}{r_port:{width}}")

a = [ 1, 2, 3, 4, 5 ]
b = [ 100, 200, 300, 400, 500 ]

access_template = [ 'switchport mode access',
                    'switchport access vlan',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable' ]

access = {'0/12': 10, '0/14': 11, '0/16': 17}

# for intf in access:
#     print("interface Gigabit" + intf)
#     for command in access_template:
#         if command.endswith('access vlan'):
#             print(f"{command} {access[intf]}")
#         else:
#             print(f"{command}")
#
# for intf ,vlan in access.items():
#     print("interface FastEthernet" + intf)
#     for commands in access_template:
#         if commands.endswith("access vlan"):
#             print("{} {}".format(commands,vlan))
#         else:
#             print("{}".format(commands))

table = [ [ '100', 'a1b2.ac10.7000', 'DYNAMIC', 'Gi0/1' ],
          [ '200', 'a0d4.cb20.7000', 'DYNAMIC', 'Gi0/2' ],
          [ '300', 'acb4.cd30.7000', 'DYNAMIC', 'Gi0/3' ],
          [ '100', 'a2bb.ec40.7000', 'DYNAMIC', 'Gi0/4' ],
          [ '500', 'aa4b.c550.7000', 'DYNAMIC', 'Gi0/5' ],
          [ '200', 'a1bb.1c60.7000', 'DYNAMIC', 'Gi0/6' ],
          [ '300', 'aa0b.cc70.7000', 'DYNAMIC', 'Gi0/7' ] ]

for vlan, mac, *other, interface in table:
    print(vlan, mac, interface)


def configure_intf(intf_name, ip, mask):
    config = f'interface {intf_name}\nip address {ip} {mask}'
    return config


print(configure_intf('fa0/1','1.1.1.1','24'))
result = configure_intf('Fa0/0', '10.1.1.1', '255.255.255.0')
print(result)