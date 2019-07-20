# Задание 6.1a

yourIP = input("Enter your IP: ")

sepIP = yourIP.split('.')

if len(sepIP) != 4:
    print('Incorrect IPv4 address')
for x in sepIP:
  if not x.isdigit():
    print('Incorrect IPv4 address')
  i = int(x)
  if i < 0 or i > 255:
    print('Incorrect IPv4 address')

sepIP = list(map(int, sepIP))

if sepIP[-1] in range(1,224):
  print('unicast')
elif sepIP[-1] in range(224,240):
  print('multicast')
elif yourIP == '255.255.255.255':
  print('local broadcast')
elif yourIP == '0.0.0.0':
  print('unassigned')
else:
  print('unused')



