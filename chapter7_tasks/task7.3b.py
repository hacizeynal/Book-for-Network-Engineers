input_vlan = int(input("Please enter VLAN ID to proceed: "))

mac_table = []

with open("CAM_table.txt") as cam_table:
    for line in cam_table:
        new_list = line.split()
        if new_list and new_list [ 0 ].isdigit():
            vlan_id, mac, other, interface_id = new_list
            mac_table.append([ int(vlan_id), mac, interface_id ])

for lists in mac_table:
    if input_vlan == lists[0]:
        print(lists)

