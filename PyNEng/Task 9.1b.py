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

    INTERF = [intf for intf, vlan in access.items()]
    PORTS_DICT = {key: [] for key in INTERF}

    if psecurity:
      for key, value in PORTS_DICT.items():
        for intf, vlan in access.items():
          PORTS = []
          for command in access_template:
            if command.endswith('access vlan'):
              PORTS.append(command + ' {}'.format(vlan))
            else:
              PORTS.append(command)
          for security_command in port_security:
            PORTS.append('* {}'.format(security_command))
        PORTS_DICT[key].append(PORTS)
    else:
      for key, value in PORTS_DICT.items():
        for intf, vlan in access.items():
          PORTS = []
          for command in access_template:
            if command.endswith('access vlan'):
              PORTS.append(command + ' {}'.format(vlan))
            else:
              PORTS.append(command)
        PORTS_DICT[key].append(PORTS)

    return PORTS_DICT



access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

# Call the function
print(generate_access_config(access_dict,True))
