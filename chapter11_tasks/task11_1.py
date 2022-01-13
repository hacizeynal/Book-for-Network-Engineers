"""


Create a function parse_cdp_neighbors that handles show cdp neighbors command output. The function must have one
parameter, command_output, which expects a single string of command output as an argument (not a filename). To do
this, you need to read the entire contents of the file into a string, and then pass the string as an argument to the
function (how to pass the command output is shown in the code below). The function should return a dictionary that
describes the connections between devices.
For example, if the following output was passed as an argument:

R4>show cdp neighbors

Device ID   Local Interface     Holdtime        Capability    Platform    Port ID
R5          Fa 0/1               111              R S I       2811        Fa 0/1
R6          Fa 0/2               143              R S I       2811        Fa 0/0

Function should return a dictionary:

 {("R4", "Fa0/1"): ("R5", "Fa0/1"),
 ("R4", "Fa0/2"): ("R6", "Fa0/0")}

In the dictionary, interfaces must be written without a space between type and name. That
is, so Fa0/0, and not so Fa 0/0. Check the operation of the function on the contents of the sh_cdp_n_sw1.txt file. In
this case, the function should work on other files (the test checks the operation of the function on the output from
sh_cdp_n_sw1.txt and sh_cdp_n_r3.txt). Restriction: All tasks must be done using the topics covered in this and
previous chapters

"""


def parse_cdp_neighbors(command_output):
    """
    Here we pass the output of the command as single string because it is in this
    form that received command output from equipment. Taking the output of
    the command as an argument, instead of a filename, we make the function more
    generic: it can work both with files and with output from equipment.
    Plus, we learn to work with such an output.
    """
    final_result = {}

    for line in command_output.split("\n"):
        line = line.rstrip().strip()
        like_column = line.split()
        if ">" in line:
            hostname = line.split(">") [ 0 ]
        elif len(like_column) >= 5 and like_column [ 3 ].isdigit():
            remote_device, local_port, local_interface_number, *other, remote_port, remote_interface_number = like_column
            final_result [
                hostname, local_port + local_interface_number ] = remote_device, remote_port + remote_interface_number
    return final_result


if __name__ == "__main__":
    with open("show_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
