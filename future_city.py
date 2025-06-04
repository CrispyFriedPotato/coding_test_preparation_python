n, m = map(int, input().split())
INF = int(1e9)
edge = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    edge[a][b] = 1
    edge[b][a] = 1
for i in range(n+1):
    edge[i][i] = 0
    
x, k = map(int, input().split())

# k를 중간에 거쳐 x로 가는 최소 이동 시간
# D1k = min(D1k, D12+D2k) ~ D13+D3k, D14+D4k...
# Dkx = min(Dkx, Dk1+D1x)...

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            edge[a][b] = min(edge[a][i]+edge[i][b], edge[a][b])

distance = edge[1][k]+edge[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)
    