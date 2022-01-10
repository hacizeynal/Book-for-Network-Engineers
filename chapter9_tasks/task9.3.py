"""
Task 9.3
Create a get_int_vlan_map function that handles the switch configuration
file and returns a tuple of two dictionaries:
* a dictionary of ports in access mode, where the keys are port numbers,
  and the access VLAN values (numbers):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}
* a dictionary of ports in trunk mode, where the keys are port numbers,
  and the values are the list of allowed VLANs (list of numbers):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}
The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.
Check the operation of the function using the config_sw1.txt file.
Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""


def get_int_vlan_map(config_filename):
    access_dictinoary = {}
    trunk_dictinoary = {}

    with open(config_filename) as full_configuration:

        for lines in full_configuration:
            lines.rstrip()
            if lines.startswith("interface"):
                interface_id = lines.split() [ -1 ]
            elif "access vlan" in lines:
                access_dictinoary [ interface_id ] = int(lines.split() [ -1 ])
            elif "allowed vlan" in lines:
                line_to_list = lines.split() [ -1 ]
                vlans = line_to_list.split(",")
                vlan_result_for_trunk = [ int(i) for i in vlans ]
                trunk_dictinoary [ interface_id ] = vlan_result_for_trunk
        return access_dictinoary, trunk_dictinoary


print(get_int_vlan_map("config_sw1.txt"))
