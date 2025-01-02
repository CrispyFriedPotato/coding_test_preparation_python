from collections import deque

def bfs(start_x, start_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(start_x, start_y)])
    visitied = set([(start_x, start_y)])
    row, col = len(graph), len(graph[0])
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<row and 0<=ny<col:
                if (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visitied.add((nx, ny))
