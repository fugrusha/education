# Задание 9.1b

def generate_access_config(access, psecurity = False):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Функция возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    '''

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
    INTERF = access.keys()
    #INTERF = [intf for intf, vlan in access.items()]
    VALUES_LIST = access.values()
    
    if psecurity:
      for vlan in VALUES_LIST:
        commands = [' {} {}'.format(command, vlan) if command.endswith('access vlan') else ' {}'.format(command) for command in access_template]
      security_commands = [' {}'.format(command) for command in port_security]
      VALUES = commands + security_commands
    else:
      for vlan in VALUES_LIST:
        commands = [' {} {}'.format(command, vlan) if command.endswith('access vlan') else ' {}'.format(command) for command in access_template]
      VALUES = commands

    PORTS_DICT = {key: VALUES for key in INTERF}
    return PORTS_DICT


access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

# Call the function
print(generate_access_config(access_dict,True))
