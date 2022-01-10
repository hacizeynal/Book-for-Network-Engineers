# From the strings command1 and command2, get a list of VLANs that exist in both command1 and command2 (intersection).
# In this case, the result should be a list: ['1', '3', '8'].
# Write the resulting list to the result variable. (this is the variable that will be checked in the test) Print the resulting list to the standard output (stdout) using print.
# Restriction: All tasks must be done using the topics covered in this and previous chapters.

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlans1 = command1.split()[-1].split(",")
vlans2 = command2.split()[-1].split(",")

result = sorted(set(vlans2) & set(vlans1))
print(result)





