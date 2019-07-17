# Задание 4.6

ospf_route = 'OSPF        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

route = ospf_route.split()

RES = '''
Protocol:               {:10}
Prefix:                 {:10}
AD/Metric:              {:10}
Next-Hop:               {:10}
Last update:            {:10}
Outbound Interface:     {:10}
'''.format(route[0], route[1], route[2], route[4], route[5].replace(',',''),route[6])

print(RES)