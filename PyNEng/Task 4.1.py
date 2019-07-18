# Задание 4.1

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(NAT.replace('FastEthernet', 'GigabitEthernet'))