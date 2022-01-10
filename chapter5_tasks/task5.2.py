# Ask the user to enter the IP network in the format: 10.1.1.0/24.
# Then print information about the network and mask in this format:

enter_ip_mask = input("Hey user ,please enter network address and mask : ")
enter_ip_mask = enter_ip_mask.split("/")
network_address = enter_ip_mask [ 0 ]
subnet_mask = enter_ip_mask [ 1 ]
network_address = network_address.split(".")
subnet_mask = int(subnet_mask)

# starting from here is used for convert network address
output_for_network = """

Network Address
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

"""

octet1, octet2, octet3, octet4 = [

    int(network_address [ 0 ]),
    int(network_address [ 1 ]),
    int(network_address [ 2 ]),
    int(network_address [ 3 ])
]

# ending of creating network address

bin_mask = "1" * subnet_mask + "0" * (32 - subnet_mask)

output_for_subnet_mask = """
Mask:
/{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:08b} {2:08b} {3:08b} {4:08b}

"""
mask1, mask2, mask3, mask4 = [
    int(bin_mask [ 0:8 ], 2),
    int(bin_mask [ 8:16 ], 2),
    int(bin_mask [ 16:24 ], 2),
    int(bin_mask [ 24:32 ], 2)
]

# printing output for network and subnet mask

print(output_for_network.format(octet1, octet2, octet3, octet4))
print(output_for_subnet_mask.format(subnet_mask, mask1, mask2, mask3, mask4))
