# Process the ospf_route string and print the information to the stdout as follows:
# Prefix     10.0.24.0/24
# AD/Metric  110/41
# Next-Hop   10.0.13.3
# Last update  3d18h
# Outbound Interface FastEthernet0/0

# Restriction: All tasks must be done using the topics covered in this and previous chapters.

ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

output = "{:<40}{}\n" * 5
# print(output)

route = ospf_route.replace(",", " ").replace("[", "").replace("]", "")
# print(route)
route = route.split()
print(route)
print(output.format(
    "Prefix", route [ 0 ],
    "AD/Metric", route [ 1 ],
    "Next-Hop", route [ 3 ],
    "Last update", route [ 4 ],
    "Outbound Interface", route [ 5 ],
))
