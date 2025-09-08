import heapq
import sys


n = int(input())
infor = list(map(int,sys.stdin.read().splitlines()))
heap = []

for i in infor:
    if i == 0:
        if not heap:
            print('0')
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(i),i))