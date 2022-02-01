"""
Task 15.3
Create a convert_ios_nat_to_asa function that converts NAT rules from
cisco IOS syntax to cisco ASA.
The function expects such arguments:
- the name of the file containing the Cisco IOS NAT rules
- the name of the file in which to write the NAT rules for the ASA
The function returns None.
Check the function on the cisco_nat_config.txt file.
Example cisco IOS NAT rules
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023
And the corresponding NAT rules for the ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023
In the file with the rules for the ASA:
- there should be no blank lines between the rules
- there must be no spaces before the lines "object network"
- there must be one space before the rest of the lines
In all rules for ASA, the interfaces will be the same (inside, outside).
"""
import re
from pprint import pprint

final_config = """
object network LOCAL_{IP}
 host {IP}
 nat (inside,outside) static interface service tcp {source_port} {dest_port}
"""
zeynal = "I love you <3  "


def convert_ios_nat_to_asa(nat_config_file, real_configuration):
    with open(nat_config_file, "r") as source_config, open(real_configuration, "w") as destination_config:
        for b in source_config:
            match_regex = re.search("(?P<IP>\d+.\.\d+\.\d+\.\d+) (?P<source_port>\d+)(?:.*) (?P<dest_port>\d+)",
                                    b)
            k = match_regex.groupdict()
            print(k)
            # ** will be used for dictionary unpacking ,values will be replaced with formatting method.
            # **kwargs is called packing of dict
            destination_config.write(final_config.format(**k))
    return zeynal


pprint(convert_ios_nat_to_asa("cisco_nat_config.txt", "real_configuration.txt"))
