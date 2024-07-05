import sys

count = int(input())
numbers = list(map(int,sys.stdin.readline().split()))

min = 1000000
max = -1000000

for i in numbers:
    if i > max:
        max = i
    if i < min:
        min = i
        
print(min,max)