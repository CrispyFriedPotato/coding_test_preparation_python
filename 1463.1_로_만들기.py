# 1463
# bfs와 DP 둘다로 문제 푸는 것이 가능하다고 한다.

n = int(input())

D = [0]*(n+1)
D[1] = 0

for i in range(2,n+1):
    D[i] = D[i-1] + 1
    
    if i%3 == 0:
        D[i] = min(D[i//3]+1, D[i])
    if i%2 == 0:
        D[i] = min(D[i//2]+1, D[i])
        
print(D[n])
    