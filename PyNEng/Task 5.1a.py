# Задание 5.1a

IP = input('Enter your IP: ')

IP = IP.split('/')

network = list(map(int, IP[0].split('.')))

if network[-1] != 0:
  network[-1] = 0
else:
  pass

mask = IP[1]

print ('-'*30)
print ('''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''.format(network[0], network[1], network[2], network[3]))

print ('''
Mask:
{}
'''.format(mask))
print ('-'*30)