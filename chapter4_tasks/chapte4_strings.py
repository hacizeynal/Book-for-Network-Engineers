"""

String in Python is:
• sequence of characters enclosed in quotes
• immutable ordered data type


"""

# String methods

string1 = 'FastEthernet'  # make everything with CAPITAL letter
print(string1.upper())

string2 = 'FastEthernet'
print(string2.lower())

string3 = 'FastEthernet'
print(string3.swapcase())

string4 = 'tunnel0'
print(string4.capitalize())

string5 = 'Hello, hello, hello, hello'
print(string5.count("ello"))

string6 = 'interface FastEthernet0/1'
print(string6.find("Fast"))

string7 = 'FastEthernet0/1'
print(string7.endswith("1"))

string8 = 'FastEthernet0/1'
print(string8.replace("Fast", "ET"))

"""
Often when a file is processed, the file is opened line by line. 
But at the end of each line, there are usually some special characters (and may be at the beginning). 
For example, new line character.
To get rid of them, it is very convenient to use method strip:
"""

string9 = '\n\tinterface FastEthernet0/1\n'
print(string9)
print(string9.strip())

string10 = '[110/1045]'

"""
Method strip removes special characters at the beginning and at the end of the line. 
If you want to remove characters only on the left or only on the right, 
you can use lstrip and rstrip.
"""

print(string10.strip("[]"))

"""
In example above, string1.split splits the string by spaces and returns a list of strings. 
The list is saved to commands variable.

"""

string11 = 'switchport trunk allowed vlan 10,20,30,100-200'
commands = string11.split()
print(commands)

ip = '10.1.1.1'
smask = 24

print(f"IP address is {ip} and mask is {smask}")
print("IP address is {} and mask is {} ==> this method is with format method".format(ip, smask))

oct1, oct2, oct3, oct4 = [ 10, 1, 1, 1 ]

s = ('Test' + 'String')
print(s)
s1 = 'Test' 'String'
print(s1)

s2 = ('Test'
      's')
print(s2)

message = ('During command execution "{}" '
           'such error occurred "{}".\n'
           'Exclude this command from the list? [y/n]')
print(message)
