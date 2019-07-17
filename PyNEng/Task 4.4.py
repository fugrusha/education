# Задание 4.4 

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

vlan1 = set(command1.split()[-1].split(','))
vlan2 = set(command2.split()[-1].split(','))

result = list(vlan1.intersection(vlan2))

listcompr = [int(i) for i in result]

print(listcompr)