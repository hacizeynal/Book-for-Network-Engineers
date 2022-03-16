"""
Task 20.4
Create a template templates/add_vlan_to_switch.txt that will be used
if you need to add a VLAN to the switch.
The template must support the following features:
* add VLAN and VLAN name
* adding VLANs as access, on the specified interface
* adding VLANs to the list of allowed, on specified trunks
The template must be created manually by copying parts of the config into
the corresponding template.
If VLAN needs to be added as access, you need to configure the interface
mode and add it to VLAN:
interface Gi0/1
  switchport mode access
  switchport access vlan 5
For trunks, you only need to add VLANs to the allowed list:
interface Gi0/10
  switchport trunk allowed vlan add 5
The variable names should be chosen based on the sample data in
the data_files/add_vlan_to_switch.yaml file.
Check the templates/add_vlan_to_switch.txt template against the data
in data_files/add_vlan_to_switch.yaml using the generate_config function
from task 20.1. Do not copy the code of the generate_config function.
"""

import yaml
from jinja2 import Environment, FileSystemLoader
import os


def generate_config(template, input_dict):
    template_directory, main_template = os.path.split(template)
    env = Environment(
        loader=FileSystemLoader(template_directory),
        trim_blocks=True,
        lstrip_blocks=True)
    final_config = env.get_template(main_template)
    return final_config.render(input_dict)


if __name__ == "__main__":
    data_file = "data_files/add_vlan_to_switch.yaml"
    template_file = "templates/add_vlan_to_switch.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
        print(data)
    print(generate_config(template_file, data))