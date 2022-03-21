import sys
import textfsm
from tabulate import tabulate

template = sys.argv[1]
output_file = sys.argv[2]

with open("show_ip_int.template") as f, open("show_ip_int.txt") as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    print(header)
    result = re_table.ParseText(output.read())
    print(result)
    print(tabulate(result, headers=header))
