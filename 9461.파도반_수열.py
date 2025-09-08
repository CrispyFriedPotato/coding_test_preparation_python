t = int(input())
for _ in range(t):
    n = int(input())
    D = [0] * (n+1)
    if n <=3:
        for i in range(1,n+1):
            D[i] = 1
        print(D[n])
    else:
        D[1] = 1
        D[2] = 1
        D[3] = 1
        for i in range(4,n+1):
            D[i] = D[i-3] + D[i-2]
        
        print(D[n])