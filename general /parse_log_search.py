import re


regex = ('Host \S+ '
         'in vlan (\d+) '
         'is flapping between port '
         '(\S+) and port (\S+)')

ports = set()

with open("log.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            vlan = match.group(1)
            # print(vlan)
            ports.add(match.group(2))
            # print(match.group(2))
            ports.add(match.group(3))
            # print(match.group(3))

print(ports)
print("Loop between ports {} in VLAN {}".format(" ,".join(ports), vlan))
