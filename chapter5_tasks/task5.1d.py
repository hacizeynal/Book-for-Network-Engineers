london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }}

ask_input = input("Enter name of device: ")
result = london_co [ ask_input ]
keys = ",".join(result)
parameter_of_network_device = (input("Please enter parameter to display ({}) :".format(keys))).lower()
final_result = result.get(parameter_of_network_device, "No such parameter")
print(final_result)

