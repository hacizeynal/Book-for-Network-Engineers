london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
print(london)

london = {
    'id': 1,
    'name': 'London',
    'it_vlan': 320,
    'user_vlan': 1010,
    'mngmt_vlan': 99,
    'to_name': None,
    'to_id': None,
    'port': 'G1/0/11'
}
print(london)
london [ 'fabric_name' ] = "ACI"
london [ 'fabric_age' ] = 2
print(type(london [ 'to_name' ]))

print(london)
print(london)
print(london [ 'user_vlan' ])

london_co = {
    'r1': {
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    }, 'r2': {
        'hostname': 'london_r2',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'hostname': 'london_sw1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101'
    }}

london_fake = london

print(id(london))
print(id(london_fake))

print(london_fake [ 'port' ])

london_copy = london_fake.copy()
print(id(london_copy))
print(id(london_fake))

# print(london_fake['amal'])
print(london_fake.get('amal', "Not found"))

print(london_fake.setdefault('itisfake'))
print(london_fake)

hecne = london_fake.setdefault("new_model", "CiscoISE")
print(london_fake)

print(london_fake.keys())
print(london_fake.values())
print(london_fake.items())
del london_fake [ 'new_model' ]
print(london_fake)

r1 = {'name': 'London1', 'location': 'London Str'}

r1.update({'vendor': 'Cisco', 'ios': '15.2'})
print(r1)

d_keys = [ 'hostname', 'location', 'vendor', 'model', 'ios', 'ip' ]
new_dic = dict.fromkeys(d_keys)
print(new_dic)


router_models = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']
model_count = dict.fromkeys(router_models, 0)
print(model_count)





router_models = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']
routers = dict.fromkeys(router_models, [])
print(routers)


routers['ISR2911'].append('londoh1')
print(routers)



