# Convert the IP address in the ip variable to binary and print output in columns to stdout: • the first line must be decimal values
# • the second line is binary values
# The output should be ordered in the same way as in the example output below:
# • in columns
# • column width 10 characters (in binary you need to add two spaces between columns to sepa- rate octets among themselves)
# Example output for address 10.1.1.1:
ip = "192.168.3.1"

str_to_list = ip.split(".")
to_binary = "{:08b} {:08b} {:08b} {:08b}".format(int(str_to_list[0]),int(str_to_list[1]),int(str_to_list[2]),int(str_to_list[3]))
print(to_binary)
