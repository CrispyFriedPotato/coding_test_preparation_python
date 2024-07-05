import sys

n, x = map(int, sys.stdin.readline().split())
sequence = list(map(int,sys.stdin.readline().split()))

for i in range(len(sequence)):
    if sequence[i] < x:
        print(sequence[i],end=" ")