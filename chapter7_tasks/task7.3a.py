mac_table = []

with open("CAM_table.txt") as cam_table:
    for line in cam_table:
        new_list = line.split()
        if new_list and new_list [ 0 ].isdigit():
            vlan_id, mac, other, interface_id = new_list
            mac_table.append([ int(vlan_id), mac, interface_id ])


for vlan_id, mac, interface_id in sorted(mac_table):
    print("{}  {}  {}".format(vlan_id,mac,interface_id))
