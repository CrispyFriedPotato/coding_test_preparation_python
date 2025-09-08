import heapq
import sys

n = int(input())
heap = []
infor = list(map(int,sys.stdin.read().splitlines()))
for i in infor:
    if i==0:
        if not heap:
            print('0')
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,i)