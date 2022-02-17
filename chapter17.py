import csv
import pprint
import json

"""
Working with CSV 
"""

# with open("show_data.csv") as k:
#     read_data = csv.reader(k)
#     headers = next(read_data)
#     print("Headers: " ,headers)
#     for row in read_data:
#         print("Rows: " ,row)

# with open("show_data.csv") as k:
#     read_data = csv.DictReader(k)
#     for row in read_data:
#         print(row)
#         print(row [ "hostname" ], row [ "modelXX" ])

data = [ [ 'hostname', 'vendor', 'model', 'location' ],
         [ 'sw1', 'Cisco', '3750', 'London, Best str' ],
         [ 'sw2', 'Cisco', '3850', 'Liverpool, Better str' ],
         [ 'sw3', 'Cisco', '3650', 'Liverpool, Better str' ],
         [ 'sw4', 'Cisco', '3650', 'London, Best str' ] ]
#
# with open("test_new_data.csv", "w") as j:
#     write_data = csv.writer(j)
#     for row in data:
#         write_data.writerow(row)
#
# with open("test_new_data.csv") as k:
#     # read_data = csv.reader(k)
#     # for row in read_data:
#     #     print(row)
#     print(k.read())

# with open("test2_new_data.csv" ,"w") as j:
#     write_data = csv.writer(j, quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         write_data.writerow(row)
#
# with open("test2_new_data.csv") as k:
#     print(k.read())

data_dict = [ {
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
} ]

# with open("csv_write_dict.csv", "w") as l:
#     writer = csv.DictWriter(l, fieldnames=list(data_dict [ 0 ].keys()), quoting=csv.QUOTE_NONNUMERIC, delimiter="?")
#     # print(list(data_dict[0].keys()))
#     # writer.writeheader()
#     for i in data_dict:
#         writer.writerow(i)

"""
Work with JSON files
"""
# json.load() will read JSON object

# with open("sw_templates.json") as k:
#     template = json.load(k)
#     print(type(template))
#     a = template.items()
#     print(a)
# for section, commands in template.items():
#     print(section)
#     print("\n".join(commands))  # join  helps to create string from any iterable

# json.loads() will return a dictionary from JSON string

# with open("sw_templates.json") as f:
#     file_content = f.read()
#     template2 = json.loads(file_content)
# print(template2)
# # print(type("sw_templates.json"))

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_json = {'trunk': trunk_template, 'access': access_template}

with open('sw2_templates.json', 'w') as m:
    m.write(json.dumps(to_json))
    print(type("sw2_templates.json"))

with open("sw2_templates.json") as n:
    print(n.read())

with open("sw3_templates.json","w") as d:
    json.dump(to_json,d)
    print(type("sw3_templates.json"))

with open("sw3_templates.json") as n:
    print(n.read())
