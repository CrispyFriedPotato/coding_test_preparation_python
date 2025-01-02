from collections import deque

def bfs(start_node, graph):
    queue = deque([start_node])
    visited = set([start_node])
    
    while queue:
        curr_node = queue.popleft()
        
        for next_node in graph[curr_node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)
                
    return -1