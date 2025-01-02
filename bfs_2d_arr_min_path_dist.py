from collections import deque

def bfs_path(start_x, start_y, end_x, end_y, graph):
    dx = [-1 ,1, 0, 0]
    dy = [0, 0, -1 ,1]
    rows, cols = len(graph), len(graph[0])
    
    queue = deque([(start_x,start_y,[(start_x, start_y)])])
    visited = set([(start_x,start_y)])
    
    while queue:
        curr_x, curr_y, path = queue.popleft()
        
        if curr_x == end_x and curr_y == end_y :
            return path
        
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if 0<=nx<rows and 0<=ny<cols:
                if (nx, ny) not in visited:
                    queue.append((nx, ny, path+[(nx, ny)]))
                    visited.add((nx, ny))
    return -1


def bfs_dist(start_x, start_y, end_x, end_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    rows, cols = len(graph), len(graph[0])
    
    queue = deque([(start_x,start_y, 1)])
    visited = set([(start_x, start_y)])
    
    while queue:
        curr_x, curr_y, dist = queue.popleft()
        
        if curr_x == end_x and curr_y == end_y:
                return dist
            
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            
            if 0<=nx<rows and 0<=ny<cols:
                if (nx, ny) not in visited:
                
                    visited.add((nx, ny)) 
                    queue.append((nx, ny, dist+1))
    return -1