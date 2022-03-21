"""
Task 21.1a
Create parse_output_to_dict function.
Function parameters:
* template is the name of the file containing the TextFSM template.
  For example templates/sh_ip_int_br.template
* command_output - output of the corresponding show command (string)
The function should return a list of dictionaries:
* keys - names of variables in the TextFSM template
* values - parts of the output that correspond to variables
Check the operation of the function on the output of the command
output/sh_ip_int_br.txt and the template templates/sh_ip_int_br.template.
"""

import textfsm


def parse_output_to_dict(template, command_output):
    with open(template) as f:
        parse_with_fsm = textfsm.TextFSM(f)
        header = parse_with_fsm.header
        # print(header)
        result = parse_with_fsm.ParseText(command_output)
        for line in result:
            print(line)
        # print(result)
    return [ dict(zip(parse_with_fsm.header, single_list)) for single_list in result ]  # list comprehension


if __name__ == "__main__":
    with open("data_files/show_ip_int_br.txt") as ready_output:
        output = ready_output.read()
    result = parse_output_to_dict("templates/show_ip_int_br.template", output)
    print(result)
