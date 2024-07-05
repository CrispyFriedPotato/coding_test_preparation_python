import sys

a , b = map(int, sys.stdin.readline().split())

A = []
B = []

for i in range(a):
    A.append(list(map(int,sys.stdin.readline().split())))

for i in range(a):
    B.append(list(map(int,sys.stdin.readline().split())))
    
for i in range(a):
    for j in range(b):
        A[i][j] += B[i][j]
        print(A[i][j],end=" ")
    print()