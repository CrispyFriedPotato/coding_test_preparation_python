n = int(input())

D = [0]*(n+1) # 0 ~ n

if n >= 1:
    D[1] = 1
    if n >=2:
        D[2] = 3

for i in range(3,n+1):
    D[i] = (D[i-2] * 2 + D[i-1])%10007

print(D[n])
    