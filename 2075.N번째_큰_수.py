import sys
import heapq

n = int(input())
heap = []
for _ in range(n):
    numbers = list(map(int,sys.stdin.readline().split()))
    for i in numbers:
        if len(heap)< n:
            heapq.heappush(heap,i)
        else:
            if heap[0] < i:
                heapq.heappushpop(heap,i)

print(heap[0])