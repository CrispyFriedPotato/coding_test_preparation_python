import sys

n = int(input())
steps = list(map(int,sys.stdin.read().splitlines()))


D = [0]*(n+1) # 1 ~ n
for i in range(1,n+1):
    D[i] += D[i-1] + steps[i-1]
    

if n>=3:
    D[3] = max(steps[0],steps[1]) + steps[2]
    for i in range(4,n+1):
        D[i] = max(D[i-2],D[i-3]+steps[i-2]) + steps[i-1]

# print(D)   
print(D[n])
