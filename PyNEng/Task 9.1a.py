# Задание 9.1a

def generate_access_config(access, psecurity=False):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    if psecurity:
      PORTS = []
      for intf, vlan in access.items():
        PORTS.append('interface {}'.format(intf))
        for command in access_template:
          if command.endswith('access vlan'):
            PORTS.append('- '+ command + ' {}'.format(vlan))
          else:
            PORTS.append('- '+ command)
        for security_command in port_security:
          PORTS.append('* {}'.format(security_command))
    else:
      PORTS = []
      for intf, vlan in access.items():
        PORTS.append('interface {}'.format(intf))
        for command in access_template:
          if command.endswith('access vlan'):
            PORTS.append('- '+ command + ' {}'.format(vlan))
          else:
            PORTS.append('- '+ command)
    return PORTS





access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

# Call the function
print('\n'.join(generate_access_config(access_dict,True)))
