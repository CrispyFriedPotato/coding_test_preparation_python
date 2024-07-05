import sys
n, m = map(int,sys.stdin.readline().split())
baskets = []

for i in range(n): #초기화
    baskets.append('0')   
    
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    for j in range(a-1,b):
        baskets[j] = c

for i in range(len(baskets)):
    print(baskets[i],end=" ") 
    