from pprint import pprint
from scrapli import Scrapli

Nexus1 = {
    "host": "10.48.75.171",
    "auth_username": "king",
    "auth_password": "Julien1991",
    "auth_strict_key": False,
    "platform": "cisco_nxos",
}


def send_show(device, show_commands):
    if type(show_commands) == str:
        show_commands = [show_commands]
    cmd_dict = {}
    with Scrapli(**Nexus1) as ssh:
        for cmd in show_commands:
            reply = ssh.send_command(cmd)
            cmd_dict[cmd] = reply.result
    return cmd_dict


if __name__ == "__main__":
    print("show".center(20, "#"))
    output = send_show(Nexus1, ["show version", "show running-config"])
    pprint(output, width=120)
