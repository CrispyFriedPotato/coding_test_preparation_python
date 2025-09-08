import sys

n = int(input())
answer = [['.']  * n for _ in range(n)] 
bomb = []

for _ in range(n):
    line = sys.stdin.readline().strip()
    a = []
    for i in range(len(line)):
        a.append(line[i])
    bomb.append(a)

bomb_loc = {}
for i in range(n):
    bomb_loc[i] = []
# making bomb_loc to dictionary
for i in range(n):
    for j in range(n):
        if bomb[i][j] == '*':
            bomb_loc[i].append(j)
            
clicked = []
for _ in range(n):
    line = sys.stdin.readline().strip()
    a = []
    for i in range(len(line)):
        a.append(line[i])
    clicked.append(a)
    

dx = [-1 ,1, 0, 0, -1,1,-1,1]
dy = [0, 0, -1, 1,-1,-1,1,1]

for i in range(n):
    for j in range(n):
        if clicked[i][j] == 'x':
            # check bomb
            if bomb[i][j] == '*':
                for x in range(n):
                    for y in bomb_loc[x]:
                        answer[x][y] = '*'
            else:
                count = 0
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if ny in bomb_loc[nx]:
                            count += 1
                        
                answer[i][j] = count

for i in range(n):
    for j in range(n):
        print(answer[i][j],end='')
    print()
                