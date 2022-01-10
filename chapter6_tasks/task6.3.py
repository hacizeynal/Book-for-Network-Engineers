access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]
access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": [ "add", "10", "20" ], "0/2": [ "only", "11", "30" ], "0/4": [ "del", "17" ]}

for interface_id, mode in trunk.items():
    print("interface FastEthernet{} ".format(interface_id))
    for commands_trunk in trunk_template:
        if commands_trunk.endswith("allowed vlan"):
            action = mode[0]
            vlans = ",".join(mode[1:])
            if action == "add":
                print("{} add {}".format(commands_trunk, vlans))
            elif action == "only":
                print("{} {}".format(commands_trunk, vlans))
            elif action == "del":
                print("{} del {}".format(commands_trunk, vlans))
        else:
            print("{}".format(commands_trunk))
