from pprint import pprint
import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_show_command(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:  # dictionary unpacking
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result [ command ] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as i:
        devices = yaml.safe_load(i)
        print(type(devices))
    for device in devices:
        result = send_show_command(device, [ "sh hostname", "show version" ])
        pprint(result, width=120)
