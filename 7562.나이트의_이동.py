from collections import deque

def bfs(start_x, start_y, dest_x, dest_y):
    dx = [-2,-1,-2, -1, 1, 2, 1,   2]
    dy = [1, 2, -1, -2, 2, 1, -2, -1]
    
    row, col = len(chess), len(chess[0])
    queue = deque([(start_x,start_y, 0)])
    visited = set([(start_x,start_y)])
    
    while queue:
        x,y,path = queue.popleft()
        
        if (x,y) == (dest_x,dest_y):
            print(path)
            return
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < row and 0 <= ny < col:
                if (nx,ny) not in visited:
                    queue.append((nx,ny,path+1))
                    visited.add((nx,ny))
    return -1
    
t = int(input())
for _ in range(t):
    l = int(input())
    chess = [[0]*l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    dest_x, dest_y = map(int,input().split())
    
    bfs(start_x, start_y, dest_x,dest_y)