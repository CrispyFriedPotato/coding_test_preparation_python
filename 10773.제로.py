from sys import stdin
k = int(stdin.readline())
numbers = []
for i in range(k):
    n = int(stdin.readline())
    if n == 0:
        numbers.pop()
    else:
        numbers.append(n)

print(sum(numbers))
        