import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))

start = 0
count = 0

while start < n:
    found = False
    #[start:end], even length
    for end in range(start+2, n+2, 2):
        segment = numbers[start:end]
        if segment == segment[::-1]:
            found = True
            count += 1
            start = end
            break
    
    if found == False:
        count = -1
        break
    
print(count)