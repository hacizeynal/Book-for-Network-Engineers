with open("CAM_table.txt") as mac_table:
    for line in mac_table:
        new_list = line.split()
        if new_list and new_list[0].isdigit():
            # mac_address = new_list[1]
            # vlan = new_list[0]
            # port_interface = new_list[3]
            mac,vlan_id ,type,port_id = new_list
            # print("{}{}{}".format(vlan, mac_address, port_interface))
            print('{:10}{:20} {}'.format(mac,vlan_id,port_id))

