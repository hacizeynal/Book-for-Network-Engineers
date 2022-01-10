"""

Create a create_network_map function that processes the show cdp neighbors command output from multiple files and
merges it into one common topology. The function must have one parameter, filenames, which expects as an argument a
list of filenames containing the output of the show cdp neighbors command. The function should return a dictionary
that describes the connections between devices. The struc- ture of the dictionary is the same as in task 11.1:

 {("R4", "Fa0/1"): ("R5", "Fa0/1"),
 ("R4", "Fa0/2"): ("R6", "Fa0/0")}

Generate topology that matches the output from the files:
• sh_cdp_n_r1.txt
• sh_cdp_n_r2.txt
• sh_cdp_n_r3.txt
• sh_cdp_n_sw1.txt

Do not copy the code of the parse_cdp_neighbors and draw_topology functions.If the parse_cdp_neighbors function
cannot process the output of one of the command output files, you need to correct the function code in task 11.1.
Restriction: All tasks must be done using the topics covered in this and previous chapters.

infiles = [
    "show_cdp_n_sw1.txt",
    "show_cdp_n_r1.txt",
    "show_cdp_n_r2.txt",
    "show_cdp_n_r3.txt",
]
"""
infiles = [
    "show_cdp_n_sw1.txt",
    "show_cdp_n_r1.txt",
    "show_cdp_n_r2.txt",
    "show_cdp_n_r3.txt",
]
from pprint import pprint


def create_network_map(all_configurations_from_devices):
    final_result = {}
    for name_of_device in infiles:
        with open(name_of_device) as configuration_of_device:
            for each_line in configuration_of_device:
                column = each_line.split()
                if ">" in each_line:
                    hostname = each_line.split(">") [ 0 ].strip().rstrip()
                elif len(column) > 5 and column [ 3 ].isdigit():
                    remote_device, local_interface, local_interface_id, *other, remote_interface, remote_interface_id = column
                    final_result [
                        hostname, local_interface + local_interface_id ] = remote_device, remote_interface + remote_interface_id

    return final_result


if __name__ == "__main__":
    pprint(create_network_map(infiles))
