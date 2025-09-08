from collections import deque
import sys

def bfs(start_x,start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue.append((start_x,start_y,[(start_x,start_y)]))
    visited.add((start_x,start_y))
    row, col = len(paper),len(paper[0])
    
    space = set([(start_x,start_y)])
    
    while queue:
        curr_x, curr_y, path = queue.popleft()
        
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            
            if 0<=nx<row and 0<=ny<col:
                if (nx,ny) not in visited and paper[nx][ny] == 1:
                    visited.add((nx,ny))
                    queue.append((nx,ny,path+[(nx,ny)]))
                    space.add((nx,ny))
    
           
    return len(space)

m, n, k = map(int, input().split())
paper = [[1]*n for _ in range(m)]
for _ in range(k):
    start_y, start_x, end_y,end_x = map(int,input().split())    
    end_x -= 1
    end_y -= 1
    for i in range(start_x,end_x+1):
        for j in range(start_y,end_y+1):
            paper[i][j] = 0

visited = set([])
queue = deque([])
count = 0
result = []
for  i in range(m):
    for j in range(n):
        if (i,j) not in visited and paper[i][j] == 1:
            result.append(bfs(i,j))
            count += 1

print(count)
for i in sorted(result):
    sys.stdout.write(str(i)+' ')
