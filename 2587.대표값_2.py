import sys

numbers = []
for i in range(5):
    numbers.append(sys.stdin.readline())
numbers.sort()
total = 0    
for i in numbers:
    total += int(i)

print(int(total/5))
print(numbers[2])
