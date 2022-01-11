"""
Task 12.1
Create a ping_ip_addresses function that checks if IP addresses are pingable.
The function expects a list of IP addresses as an argument.
The function must return a tuple with two lists:
* list of available IP addresses
* list of unavailable IP addresses
To check the availability of an IP address, use the ping command.
Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

import subprocess

list_of_ip_addresses = [ "11.1.1.1", "2.2.2.2", "3.3.33.3", "8.8.8.8", "4.2.2.2", "9.9.9.9", "5.5.5.5", "3.1.1.1" ]

reachable = [ ]
unreachable = [ ]


def ping_ip_addresses(hosts_to_check):
    for ip in hosts_to_check:
        reply = subprocess.run([ 'ping', '-c', '1', '-n', ip ],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               encoding='utf-8')
        if reply.returncode == 0:
            if "unreachable" in str(reply.stdout):
                unreachable.append(ip)
            else:
                reachable.append(ip)
        else:
            unreachable.append(ip)

    return unreachable, reachable


print(ping_ip_addresses(list_of_ip_addresses))
