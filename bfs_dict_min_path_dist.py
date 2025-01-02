from collections import deque

def bfs_path(start_node, end_node, graph):
    queue = deque([start_node])
    visited = set([start_node])
    path = {start_node : [start_node]}
    
    while queue:        
       curr_node = queue.popleft()
       
       if curr_node == end_node:
           return path[curr_node]
       
       for next_node in graph[curr_node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)
                path[next_node]= path[curr_node] + path[next_node]
    
    return -1


def bfs_dist(start_node,end_node, graph):
    queue = deque([start_node])
    visited = set([start_node])
    dist = {start_node : 0}
    
    while queue:
        curr_node = queue.popleft()
        
        if curr_node == end_node:
            return dist[curr_node]
        
        for next_node in graph[curr_node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)
                dist[next_node] = dist[curr_node] + 1
                
    return -1