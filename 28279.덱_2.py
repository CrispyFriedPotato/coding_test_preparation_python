from collections import deque
import sys

n = int(input())
order = sys.stdin.read().splitlines()

queue = deque([])

for i in order:
    if len(i)>1:
        if i.split()[0] == '1':
            queue.appendleft(i.split()[1])
        else:
            queue.append(i.split()[1])
    else:
        if i=='3':
            if queue:
                sys.stdout.write(str(queue.popleft())+'\n')
            else:
                sys.stdout.write(str(-1)+'\n')
        elif i=='4':
            if queue:
                sys.stdout.write(str(queue.pop())+'\n')
            else:
                sys.stdout.write('-1'+'\n')
        elif i=='5':
            sys.stdout.write(str(len(queue))+'\n')
        elif i=='6':
            if queue:
                sys.stdout.write('0'+'\n')
            else:
                sys.stdout.write('1'+'\n')
        elif i=='7':
            if queue:
                sys.stdout.write(str(queue[0])+'\n')
            else:
                sys.stdout.write('-1'+'\n')
        elif i=='8':
            if queue:
                sys.stdout.write(str(queue[-1])+'\n')
            else:
                sys.stdout.write('-1'+'\n')
                    