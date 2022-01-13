"""
Task 12.3
Create a function print_ip_table that prints a table of available
and unavailable IP addresses.
The function expects two lists as arguments:
* list of available IP addresses
* list of unavailable IP addresses
The result of the function is printing a table to the stdout:
Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9
"""

from tabulate import tabulate

unreachable = [ '11.1.1.1', '2.2.2.2', '3.3.33.3', '4.5.5.5', '3.1.1.1' ]
reachable = [ '8.8.8.8', '4.2.2.2', '9.9.9.9' ]


def print_ip_table(a, b):
    a = {"Unreachable": list(unreachable)}
    b = {"Reachable": list(reachable)}
    # merged_dic = dict(a, **b)
    c = a.copy()
    b.update(c)
    print(b)
    return tabulate(b, headers="keys", tablefmt="grid")
    # return tabulate(merged_dic, headers="keys", tablefmt="grid")


if __name__ == "__main__":
    print(print_ip_table(unreachable, reachable))
