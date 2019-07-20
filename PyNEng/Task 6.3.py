access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'}, 
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

for intf, trunk in fast_int['trunk'].items():
    print('interface FastEthernet ' + intf)
    for command in trunk_template:
        if intf == '0/4':
            print('- {} {} {}'.format(command, trunk[0], trunk[1]))
        else:
            print('- {} {} {}, {}'.format(command, trunk[0], trunk[1], trunk[2]))