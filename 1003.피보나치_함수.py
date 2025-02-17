import sys
T = int(input())

for _ in range(T):
    n  = int(input())
    D = [[0,0]]*(n+1)
    D[0] = [1,0]
    if n > 0 :
        D[1] = [0,1]
        
    
    if n ==0 or n==1:
        print(str(D[n][0])+' '+str(D[n][1]))
    else:
        for i in range(2,n+1):
            D[i] = [D[i-1][0]+D[i-2][0],D[i-1][1]+D[i-2][1]]
        # print(D)
        print(str(D[n-1][0]+D[n-2][0])+' '+str(D[n-1][1]+D[n-2][1]))    