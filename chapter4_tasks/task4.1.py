# Using the prepared nat string, get a new string where the FastEthernet interface is replaced with GigabitEthernet.
# Print the resulting new string to the standard output (stdout) using print.
# Restriction: All tasks must be done using the topics covered in this and previous chapters.

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

nat = nat.replace("FastEthernet", "GigabitEthernet")
print(nat)

