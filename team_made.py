def union_team(parent, a, b):
    a = find_team(parent, a)
    b = find_team(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
def find_team(parent, a):
    if parent[a] != a:
        parent[a] = find_team(parent, parent[a])
    return parent[a]

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    if x == 0:
        union_team(parent,y,z)
    else:
        if find_team(parent,y) != find_team(parent,z):
            print("NO")
        else:
            print("YES")        