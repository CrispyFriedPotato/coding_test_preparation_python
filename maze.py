# 이것이 취업을 위한 코딩테스트이다
# 미로탈출


from collections import deque



def bfs(visited, queue):
    
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or n-1 < nx or ny < 0 or m-1 < ny:
                continue
            if graph[nx][ny] == 0:
                continue
            if (nx,ny) in visited:
                continue
            
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx,ny))
            visited.add((nx, ny))
    return graph[n-1][m-1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = set((0,0))
queue = deque([(0,0)])

print(bfs(visited, queue))
