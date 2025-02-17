import sys
from collections import deque

def bfs_min_path(start_x,start_y, end_x, end_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    
    visited = set([(start_x,start_y)])
    queue = deque([(start_x,start_y,1)])
                  
    rows, cols = len(graph), len(graph[0])
    
    while queue:
        curr_x, curr_y, dist = queue.popleft()
        if curr_x == end_x and curr_y == end_y:
            return dist
        
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            
            if 0<=nx < rows and 0<=ny < cols:
                if graph[nx][ny]==1 and (nx,ny) not in visited:
                    queue.append((nx,ny,dist+1))
                    visited.add((nx,ny))
    
    return -1                

n, m = map(int, input().split())
maze = [[i]  for i in sys.stdin.read().splitlines()]
 
for idx, i in enumerate(maze):
    line = []
    for j in i[0]:
        line.append(int(j))
    maze[idx] = line
    
print(bfs_min_path(0,0,n-1,m-1,maze))
    


