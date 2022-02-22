"""
Task 17.2
In this task you need:
* take the contents of several files with the output of the sh version command
* parse command output using regular expressions and get device information
* write this information to a file in CSV format
To complete the task, you need to create two functions.
parse_sh_version function:
* expects the output of the sh version command as an argument in single string (not a filename)
* processes output using regular expressions
* returns a tuple of three elements:
 * ios - "12.4(5)T"
 * image - "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - "5 days, 3 hours, 3 minutes"
The write_inventory_to_csv function must have two parameters:
* data_filenames - expects a list of filenames as an argument with
  the output of sh version
* csv_filename - expects as an argument the name of a file (for example,
  routers_inventory.csv) to which information will be written in CSV format
write_inventory_to_csv function writes the contents to a file, in CSV format and returns nothing.
The write_inventory_to_csv function should do the following:
* process information from each file with sh version output:
  sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* using the parse_sh_version function, ios, image, uptime information
  should be obtained from each output
* from the file name you need to get the hostname
* after that all information should be written to a CSV file
The routers_inventory.csv file should have the following columns (in this order):
* hostname, ios, image, uptime
The code below has created a list of files using the glob module.
You can uncomment the print(sh_version_files) line to see the content of the list.
In addition, a list of headers has been created, which should be written to CSV.
"""
import re
import csv
import glob

regex_pattern = (r'Cisco IOS .*? Version (?P<ios>\S+), .*'
                 r'uptime is (?P<uptime>[\S ]+).*'
                 r'image file is "(?P<image>\S+).*')


def parse_sh_version(show_version):
    with open(show_version) as a:
        find_matches = re.search(regex_pattern, a.read(), re.DOTALL, )  # DOTALL will be used to new line character as
        # well.
        return find_matches.groups()


# print(parse_sh_version("show_version_r1.txt"))


def write_inventory_to_csv(data_filenames, csv_output):
    with open(csv_output, "w") as m:
        write_to_csv_data = csv.writer(m)
        write_to_csv_data.writerow([ "hostname", "ios", "image", "uptime" ])  # add those headers to the csv
        for device_output in data_filenames:
            hostname = re.search(r"show_version_([\S ]+).txt", device_output).group(1)  # grab hostname from filename
            # and take it
            # with group()
            with open(device_output) as k:
                grab_data_from_output = parse_sh_version(k.read())  # call first function to grab data ( expected
                # result is tuple of elements)
                if grab_data_from_output:
                    write_to_csv_data.writerow((hostname,) + parse_sh_version(device_output))  # concatenate tuple to
                    # tuple ,we are calling first function to get regex match


if __name__ == "__main__":
    sh_version_files = glob.glob("show_vers*")
    print(write_inventory_to_csv(sh_version_files, "router_inventory.csv"))
