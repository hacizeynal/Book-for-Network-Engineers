"""
Task 21.1
Create parse_command_output function. Function parameters:
* template - name of the file containing the TextFSM template.
  For example templates/sh_ip_int_br.template
* command_output - output the corresponding show command (string)
The function should return a list:
* the first element is a list with column names
* the rest of the items are lists, which contain the results
  of processing the output of the show command
Check the operation of the function on the output of the sh ip int br command
from the equipment and on the templates/sh_ip_int_br.template template.
"""
import textfsm
from netmiko import ConnectHandler


def parse_command_output(template, command_output):
    with open(template) as f:
        parse_with_fsm = textfsm.TextFSM(f)
        header = parse_with_fsm.header
        result = parse_with_fsm.ParseText(command_output)
    return [header] + result


if __name__ == "__main__":
    autopod_params = {
        "device_type": "cisco_ios",
        "host": "10.197.175.3",
        "username": "king",
        "password": "Julien1991",
        "secret": "cisco",
    }
    with ConnectHandler(**autopod_params) as ssh_to_autopod:
        ssh_to_autopod.enable()
        output = ssh_to_autopod.send_command("show ip int brief | exclude un")
    # with open("data_files/show_ip_int_br.txt") as ready_output:
    #     output = ready_output.read()
    result = parse_command_output("templates/show_ip_int_br.template", output)
    print(result)
