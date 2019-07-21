from sys import argv

file = argv[1]

with open (file, 'r+') as f:
    for line in f:
        if not line.startswith('!'):
            print(line.rstrip())
        else:
            pass