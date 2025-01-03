from collections import deque
from sys import stdin

n = int(stdin.readline())
for i in range(n):
    queue = []
    ps = stdin.readline().strip()
    for j in ps:
        if j == '(':
            queue.append(j)
        else:
            if queue:
                queue.pop()
            else: # if queue empty
                print('NO')
                break
    else:
        if queue: #not empty
            print('NO')
        else:
            print('YES')
        