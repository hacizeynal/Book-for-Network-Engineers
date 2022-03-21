"""
Task 21.2
Create a TextFSM template to parse the output of the sh ip dhcp snooping binding
command and write it to templates/sh_ip_dhcp_snooping.template
The command output is located in the file output/sh_ip_dhcp_snooping.txt.
The template should process and return the values of such columns:
* mac - 00:04:A3:3E:5B:69
* ip - 10.1.10.6
* vlan - 10
* intf - FastEthernet0/10
Check the work of the template using the parse_command_output function
from task 21.1.
"""

import textfsm


def parse_command_output(template, command_output):
    with open(template) as f:
        parse_with_fsm = textfsm.TextFSM(f)
        header = parse_with_fsm.header
        result = parse_with_fsm.ParseText(command_output)
    return [ header ] + result


if __name__ == "__main__":
    with open("data_files/sh_ip_dhcp_snooping.txt") as ready_output:
        output = ready_output.read()
    result = parse_command_output("templates/sh_ip_dhcp_snooping.template", output)
    print(result)
