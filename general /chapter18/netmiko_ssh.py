from pprint import pprint
import json
from getpass import getpass
import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

result = {}


def send_show_command(device, commands):
    try:
        with ConnectHandler(**device) as ssh:  # dictionary unpacking
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command,use_textfsm=True)
                result [ command ] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as i:
        devices = yaml.safe_load(i)
    for device in devices:
        result = send_show_command(device, [ "show hostname", "show ip interface brief " ])
        print(result)
        with open("netmiko_output.txt", "a") as l:
            l.write(json.dumps(result))

# net_connect = ConnectHandler(host="10.48.75.171", username="king", password=getpass(), device_type="cisco_nxos")
# net_connect.find_prompt()
# result = net_connect.send_command("show ip interface brief", use_textfsm=True)
# for up_interfaces in result:
#     if up_interfaces [ 'proto' ] == "protocol-up":
#         print("Interface {} is up ".format(up_interfaces ['intf']))
