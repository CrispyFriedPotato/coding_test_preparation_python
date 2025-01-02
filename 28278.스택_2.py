from collections import deque
from sys import stdin,stdout

n = stdin.readline()
queue = deque([])
for i in range(int(n)):
    choice = stdin.readline().strip()
    if choice == '2':
        if queue: #not empty
            stdout.write(str(queue.pop())+'\n')
        else:
            stdout.write('-1'+'\n')
    elif choice == '3':
        stdout.write(str(len(queue))+'\n')
    elif choice == '4':
        if queue:
            stdout.write('0'+'\n')
        else:
            stdout.write('1'+'\n')
    elif choice == '5':
        if queue:
            stdout.write(str(queue[-1])+'\n')
        else:
            stdout.write('-1'+'\n')
    else:
        _, m = map(int, choice.split())
        queue.append(m)