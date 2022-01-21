tuple1 = tuple()
print(tuple1)
print(type(tuple1))

tuple2 = ('password',)
print(tuple2)

list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
tuple_keys = tuple(list_keys)
print(tuple_keys)
print(tuple_keys[2])


b = int("11111111")
print(b)


line = "switchport trunk allowed vlan 10*20,30"
words = line.split()
print(line.split())

vlans_str = words[-1]

vlans1 = vlans_str.split()
vlans2 = vlans_str.split(',')
print(vlans1)
print(vlans2)


