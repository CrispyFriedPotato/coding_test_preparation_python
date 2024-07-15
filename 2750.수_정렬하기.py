import sys
lines = int(sys.stdin.readline())

numbers = []
for i in range(lines):
    numbers.append(int(sys.stdin.readline()))
   
# Bubble Sort
for i in range(1,len(numbers)):
    for j in range(len(numbers)-i):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
        
for i in numbers:
    print(i)