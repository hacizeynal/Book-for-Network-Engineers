import csv
import re

"""

Create the write_dhcp_snooping_to_csv function, which processes the output of the show dhcp snooping binding command
from different files and writes the processed data to the csv file.

Function arguments:

filenames - list of filenames with “show dhcp snooping binding” command output
output - the name of the csv file into which the result will be written
The function returns None.

For example, if a list with one file sw3_dhcp_snooping.txt was passed as an argument:

MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2
The resulting csv file should contain the following content:

switch,mac,ip,vlan,interface 
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20 
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21 

The first column in the csv file, the name of the switch, must be obtained from the file name,
the rest - from the contents in the files.

Check the function on the contents of the files sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.



"""
regex = re.compile("(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<interface>\S+)")


def write_dhcp_snooping_to_csv(configfile_from_device, csv_output):
    with open(configfile_from_device) as k:
        catch_from_file = regex.findall(k.read())  # find all patterns and collect them to the list of tuples
    with open(csv_output, "w") as m:
        write_data = csv.writer(m)
        write_data.writerow([ "switch", "mac", "ip", "vlan", "interface" ])  # add those headers to the csv
        hostname = re.search("dhcp_snooping_([^/]+).txt", configfile_from_device)  # grab hostname from filename
        hostname = hostname.group(1)  # this will give exact hostname ,otherwise it is match object
        for i in catch_from_file:
            print((hostname,) + i)
            write_data.writerow((hostname,) + i)


if __name__ == "__main__":
    print(write_dhcp_snooping_to_csv("dhcp_snooping_sw3.txt", "sw3_dhcp_snooping.csv"))
