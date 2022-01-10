# Get the following list of VLANs from the config string: ["1", "3", "10", "20", "30", "100"]
# Write the resulting list to the result variable. (this is the variable that will be checked in the test)
# Print the resulting list to the standard output (stdout) using print.
# Here is a very important point that you need to get exactly the list (data type), and not, for example, a string that looks like the list shown.
# Restriction: All tasks must be done using the topics covered in this and previous chapters.

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config = config.split()
print(config)
result = config[-1]
result = result.split(",")
print(result)
