#Dijkstra Algorithm with heap
import heapq

INF = int(1e9)

node, edge, start = map(int, input().split())
distance = [INF]*(node+1)
graph = [[]*(node+1) for _ in range(node+1)]
# answer sheet 
# graph = [[] for i in range(node+1)]


for _ in range(edge):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
    
    
q = []

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q,(0, start))
    while q:
        dist, now = heapq.heappop(q)
        # answer sheet
        # if distance[now] < dist:
        #       continue
        
        for y in graph[now]:
            cost = y[1] + dist
            if cost  < distance[y[0]]:
                distance[y[0]] = cost
                heapq.heappush(q,(cost,y[0]))
    

dijkstra(start)
max_dist = 0
count = 0
for i in distance:
    if i != INF:
        count +=1
        max_dist = max(max_dist,i)

print(count-1, max_dist)