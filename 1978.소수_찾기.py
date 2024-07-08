import sys

count = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
prime = 0

for i in range(len(numbers)):
    total = 0 
    if numbers[i] == 1:
        continue
    else:
        for j in range(2,int(numbers[i]**(1/2)+1)):
            if numbers[i] % j == 0:
                total +=1
        if total == 0:
            prime +=1   
print(prime)
    