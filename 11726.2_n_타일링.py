n = int(input())

D=[0]*(n+1)
for i in range(1,n+1):
    D[i] = i

for i in range(3,n+1):
    D[i] = (D[i-1]+D[i-2])%10007
print(D[n])