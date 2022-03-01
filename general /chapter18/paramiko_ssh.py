import paramiko
import time
import socket
from pprint import pprint


def send_show_command(ip, username, password, command, max_bytes=60000, short_pause=1, long_pause=5, ):
    client = paramiko.SSHClient()  # create SSH client
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # it indicates which policy to use when connecting
    # to a server whose key is unknown.
    client.connect(hostname=ip, username=username, password=password, look_for_keys=False, allow_agent=False, )  #
    # connect to device ,look_for_keys=false means we will have username/pass authentication ,paramiko can connect to
    # a local SSH agent. This is necessary when working with keys and since in this case authentication is done by
    # login/password, it should be disabled.
    with client.invoke_shell() as ssh:  # After execution of previous command there is already a connection to server.
        # Method invoke_shell allows to set an interactive SSH session with server.
        ssh.send("terminal length 0\n")
        time.sleep(short_pause)
        # ssh.send("configure terminal\n")
        # time.sleep(short_pause)
        ssh.recv(max_bytes)

        result = {}
        for command in commands:
            ssh.send(f"{command}\n")
            ssh.settimeout(5)

            output = ""
            while True:
                try:
                    part = ssh.recv(max_bytes).decode("utf-8")
                    output = part + output
                    time.sleep(0.5)
                except socket.timeout:
                    break
            result [ command ] = output

        return result


if __name__ == "__main__":
    # devices = [ "10.48.75.171", "10.48.75.172", "10.48.75.173"]
    commands = [ "show ip interface brief", "show vrf" ]
    result = send_show_command("10.48.75.171", "king", "Julien1991", commands)
    pprint(result, width=120)
