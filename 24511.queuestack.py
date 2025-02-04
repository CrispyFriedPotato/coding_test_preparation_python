import sys
from collections import deque

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
d = deque([j for i,j in zip(a,b) if i==0 ])

m = int(input())
c = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    d.appendleft(c[i])
for i in range(m):
    sys.stdout.write(str(d.pop())+' ')
