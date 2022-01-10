# import time
#
# for num in range(10):
#     print(num, end=' ')
#     time.sleep(1)

# a = [ 1, 2, 3 ]
# b = [ 100, 200, 300 ]
# print(list(zip(a, b)))
# print(zip(a, b))
#
# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4','10.255.0.1']
#
# sum = dict(zip(d_keys,d_values))
# print(sum)

d_keys = [ 'hostname', 'location', 'vendor', 'model', 'IOS', 'IP' ]

data = {'r1': [ 'london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1' ],
        'r2': [ 'london_r2', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.2' ],
        'sw1': [ 'london_sw1', '21 New Globe Walk', 'Cisco', '3850', '3.6.XE', '10.255.0.101' ]}

# london_co = {}
#
# for k in data.keys():
#     london_co [ k ] = dict(zip(d_keys, data [ k ]))
# print(london_co)
#
# list_of_tuples = [ ('IT_VLAN', 320), ('Mngmt_VLAN', 99), ('User_VLAN', 1010), ('DB_VLAN', 11) ]
# print(list_of_tuples)
# print(sorted(list_of_tuples, key=lambda x: x [ 1 ]))
#
# vlans = [ 100, 110, 150, 200, 201, 202 ]
# print(list(map(lambda z: "vlan {}".format(z), vlans)))
#
# for each_vlan in vlans:
#     print("VLAN {}".format(each_vlan))

nums = [ 1, 2, 3, 4, 5 ]
nums2 = [ 1, 4, 5, 6, 7, 7 ]

number_mul = list(map(lambda x, y: x ** y, nums, nums2))
print(number_mul)
