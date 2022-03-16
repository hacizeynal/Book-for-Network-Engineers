j = {'process': 10, 'router_id': '10.0.0.1', 'ref_bw': 20000, 'ospf_intf':
    [{'name': 'Fa0/1', 'ip': '10.255.0.1', 'area': 0, 'passive': False}, {'name': 'Fa0/1.100', 'ip': '10.255.1.1', 'area': 0, 'passive': False},
     {'name': 'Fa0/1.200', 'ip': '10.255.2.1', 'area': 0, 'passive': False}, {'name': 'Fa0/0.10', 'ip': '10.0.10.1', 'area': 2, 'passive': True},
     {'name': 'Fa0/0.20', 'ip': '10.0.20.1', 'area': 2, 'passive': True}]}

a = [{'name': 'Fa0/1', 'ip': '10.255.0.1', 'area': 0, 'passive': False}, {'name': 'Fa0/1.100', 'ip': '10.255.1.1', 'area': 0, 'passive': False},
     {'name': 'Fa0/1.200', 'ip': '10.255.2.1', 'area': 0, 'passive': False}, {'name': 'Fa0/0.10', 'ip': '10.0.10.1', 'area': 2, 'passive': True},
     {'name': 'Fa0/0.20', 'ip': '10.0.20.1', 'area': 2, 'passive': True}]

k = {'Fa0/1': {'action': 'add', 'vlans': '10,20'},
            'Fa0/2': {'action': 'only', 'vlans': '10,30'},
            'Fa0/3': {'action': 'delete', 'vlans': 10}}

for i in k:
    print(i)
