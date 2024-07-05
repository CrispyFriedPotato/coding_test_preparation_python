import sys

count = int(input())
for i in range(count):
    a,b= sys.stdin.readline().split()
    
    for j in range(len(b)):
        for i in range(int(a)):
            print(b[j],end='')
    print()