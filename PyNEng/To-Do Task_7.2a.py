from sys import argv

file = argv[1]
ignore = ['log', 'ssh', 'ip domain']

with open (file, 'r') as f:
    ignore = ['log', 'ssh', 'ip domain']
    for item in ignore:
        for line in f:
            if not '!' in line and item not in line:
                print(line.rstrip())
            else:
                pass