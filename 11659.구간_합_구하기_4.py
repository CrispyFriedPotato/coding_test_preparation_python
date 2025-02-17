import sys

n, m = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))

D = [0]*(n+1)
D[1] = numbers[0]
for i in range(2,n+1): # O(N) --- Worst: 10^5
    D[i] = D[i-1] + numbers[i-1]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    
    print(D[b]-D[a-1])
    