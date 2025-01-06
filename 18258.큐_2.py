from collections import deque
import sys

n = int(input()) # number of commands
queue = deque([])
# popleft() 시간이 오래 걸리는건가. O(1)이다.
for i in range(n):
    command = sys.stdin.readline().split() #input()이 문제였다.
    if 'push' == command[0]:
        queue.append(command[1])
    elif 'pop' == command[0]:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif 'size'== command[0]:
        print(len(queue))
    elif 'empty' == command[0]:
        if queue:
            print(0)
        else:
            print(1)
    elif 'front' == command[0]:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif 'back' == command[0]:
        if queue:
            print(queue[-1])
        else:
            print(-1)