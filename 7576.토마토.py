import sys
from collections import deque

        
m, n = map(int,input().split())
tomato = [list(map(int,i.split())) for i in sys.stdin.read().splitlines()]
day  = 0
tomato_flag = 0
dx = [ -1, 1, 0, 0]
dy = [0, 0, -1 ,1]
days = 0
queue = deque([])
visited = set([])

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            tomato_flag = 1
            queue.append((i,j,0))
            visited.add((i,j))

rows, cols = len(tomato), len(tomato[0])

while queue:
    curr_x, curr_y, day = queue.popleft()
    for i in range(4):
        nx = curr_x + dx[i]
        ny = curr_y + dy[i]
        if 0<=nx<rows and 0<=ny<cols:
            if tomato[nx][ny] == 0 and (nx,ny) not in visited:
                tomato[nx][ny] = 1
                queue.append((nx,ny,day+1))
                visited.add((nx,ny))
                days = day + 1

# 다 돌고 나서도 0이 남아있는가
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            tomato_flag = -1

if tomato_flag == 0:
    print('0')
elif tomato_flag == -1:
    print('-1')
else:
    print(day)