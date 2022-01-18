import re

log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 ' \
      'and port Gi0/15 '
log2 = '%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24'

match = re.search('Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)', log)
match2 = re.search('Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)', log2)

print(match2)
print(match2.groups())

regex = ('Host \S+ '
         'in vlan (\d+) '
         'is flapping between port '
         '(\S+) and port (\S+)')

ports = set()

with open("log.txt") as f:
    for line in f:
        match3 = re.search(regex, line)
        if match3:
            vlan = match3.group(1)
            ports.add(match3.group(2))
            ports.add(match3.group(3))

print(" Loop between ports {} {}".format(" ,".join(ports), vlan))
