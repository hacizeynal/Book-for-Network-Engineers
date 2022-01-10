access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

general_template = {"access": access_template, "trunk": trunk_template}
questions_per_mode = {"access": 'Please Enter VLAN number :', "trunk": 'Please Enter the allowed VLANs :'}


interface_mode = input("Please enter interface mode (access/trunk) : ")
interface_type_number = input("Please enter interface type and number : ")
id_of_vlan = input(questions_per_mode[interface_mode])
print('\n' + '*' * 30)
print('interface {}'.format(interface_type_number))
print('\n'.join(general_template [ interface_mode ]).format(id_of_vlan))
print('*' * 30)