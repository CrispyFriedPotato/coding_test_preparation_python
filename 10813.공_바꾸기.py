import sys
n, m = map(int,sys.stdin.readline().split())

balls = []
for i in range(1,n+1):
    balls.append(i)

for j in range(1,m+1):
    a, b = map(int,sys.stdin.readline().split())
    temp = 0
    temp = balls[a-1]
    balls[a-1] = balls[b-1]
    balls[b-1] = temp

for i in range(n):
    print(balls[i],end=" ")