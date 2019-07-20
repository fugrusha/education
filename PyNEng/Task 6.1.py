# Задание 6.1

yourIP = input("Enter your IP: ")

sepIP = yourIP.split('.')
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



