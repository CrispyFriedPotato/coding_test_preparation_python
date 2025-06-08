def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
        
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

# indegree = [0]*(n+1)
parent = [i for i in range(n+1)]

edges= []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    # indegree[a] += 1
    # indegree[b] += 1
    # graph[a].append((b,c))
    # graph[b].append((a,c))

edges.sort()
result = 0
last = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost
        last = cost


print(result - last)
    