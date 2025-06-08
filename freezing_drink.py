# import sys
# from collections import deque

# def bfs(visited,graph,i):
#     pass


# n, m = map(int, input().split())
# container = [[int(i) for i in line] for line in sys.stdin.read().splitlines()]

# visited = [[0 for i in range(m)] for j in range(n)]

# samsung version. no sys

# def bfs(graph,start,visited):
    
from collections import deque

def bfs(graph, queue, visited):
    start = queue.popleft()

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    for i in range(4):
        nx = start[0] + dx[i]
        ny = start[1] + dy[i]
        if 0<=nx<=n-1 and 0<=ny<=m-1:
            if (nx,ny) not in visited and graph[nx][ny]==0:
                visited.add((nx,ny))
                queue.append([nx,ny])
                bfs(graph,queue,visited)
    
    return
    
                
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
                 
    
# visited = [[False for i in range(m)] for j in range(n)]
visited = set()
queue = deque([])
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and (i,j) not in visited:
                visited.add((i,j))
                queue.append([i,j])
                bfs(graph, queue, visited)
                count += 1

print(count)
