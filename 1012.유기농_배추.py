from collections import deque

# 그림 개수 세기
def bfs(start,end):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    row, col = len(land), len(land[0])
    
    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            
            if 0<=nx<row and 0<=ny<col:
                if (nx,ny) not in visited and land[nx][ny] == 1:
                    queue.append((nx,ny))
                    visited.add((nx,ny))
                    
                        
n = int(input())
for _ in range(n):
    row, col, cabbage = map(int, input().split())
    land = [[0]*col for _ in range(row)] # deep copy
    for _ in range(cabbage):
        x, y = map(int, input().split())
        land[x][y] = 1
    queue = deque([])
    visited = set([])
    count = 0
    for x in range(row):
        for y in range(col):
            if land[x][y] == 1 and (x,y) not in visited:
                queue.append((x,y))
                visited.add((x,y))
                bfs(x,y)
                count += 1
    
    print(count)
                
            