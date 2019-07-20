# Задание 6.1b

yourIP = input('Enter your IP: ')
sepIP = yourIP.split('.')
sepIP = list(map(int, sepIP))

if len(sepIP) != 4:
    print('Incorrect IPv4 address')
    yourIP = input('Enter your IP one more time: ')
for x in sepIP:
    if x < 0 or x > 255:
        yourIP = input('Enter your IP one more time: ')
    else:
        print('Your IP is correct')
        break

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



