from collections import deque

# bfs distance


def bfs(start,end):
    # dx = [-1,1,2]
    queue = deque([(start,0)])
    visited = set([start])
    while queue:
        x, time = queue.popleft()
        if x == end:
            print(time)
        nx = [x+1, x-1, 2*x]
        for new_x in nx:
            if 0 <= new_x <= 100000:
                if new_x not in visited:
                    queue.append((new_x,time+1))
                    visited.add(new_x)
            
    
n , k = map(int, input().split())
bfs(n,k)


