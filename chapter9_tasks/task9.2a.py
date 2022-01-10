"""
Task 9.2a
Make a copy of the code from the task 9.2.
Change the function so that it returns a dictionary instead of a list of commands:
- keys: interface names, like 'FastEthernet0/1'
- values: the list of commands that you need execute on this interface
Check the operation of the function using the example of the trunk_config
dictionary and the trunk_mode_template template.
An example of a final dict (each string is written on a new line for readability):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}
Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [ 10, 20, 30 ],
    "FastEthernet0/2": [ 11, 30 ],
    "FastEthernet0/4": [ 17 ]
}

final_trunk_configuration_dict = {}
trunk_configuration_list = [ ]


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    for interface, vlan in intf_vlan_mapping.items():
        trunk_configuration_list.clear()  # empty list
        for config in trunk_template:
            if config.endswith("allowed vlan"):
                vlans_to_string = ",".join(str(vlans) for vlans in vlan)
                trunk_configuration_list.append(f"{config} {vlans_to_string}")
            else:
                trunk_configuration_list.append(f"{config}")
            final_trunk_configuration_dict [ interface ] = trunk_configuration_list
    return final_trunk_configuration_dict


print(generate_trunk_config(trunk_config, trunk_mode_template))

