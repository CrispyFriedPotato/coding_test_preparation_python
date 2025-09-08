import heapq

pq = []
n, m = map(int,input().split())
presents = list(map(int,input().split()))
want = list(map(int,input().split()))

for i in range(n):
    heapq.heappush(pq,-presents[i])

flag = 1
for i in range(m):
    val = -heapq.heappop(pq)
    if val >= want[i]:
        heapq.heappush(pq,-(val-want[i]))
    else:
        flag = 0
        break
if flag:
    print(1)
else:
    print(0)