while True:
    input_vlan = input("Please enter VLAN ID to proceed: ")
    correct_vlan = False

    with open("CAM_table.txt", "r") as cam_table:
        for line in cam_table:
            new_list = line.split()
            if new_list and new_list[0].isdigit() and new_list[0] == input_vlan:
                vlan_id, mac, other, interface_id = new_list
                correct_vlan = True
                print("{} {} {}".format(vlan_id, mac, interface_id))

    if correct_vlan:
        break
    else:
        print("Incorrect VLAN ,please enter VLAN ID again: ")

