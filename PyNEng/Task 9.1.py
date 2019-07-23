# Задание 9.1

def generate_access_config(access):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access
    с конфигурацией на основе шаблона
    '''
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    PORTS = []
    for intf, vlan in access.items():
      PORTS.append('interface {}'.format(intf))
      for command in access_template:
        if command.endswith('access vlan'):
          PORTS.append(command + ' {}'.format(vlan))
        else:
          PORTS.append(command)
    return PORTS





access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

# Call the function
print('\n'.join(generate_access_config(access_dict)))
