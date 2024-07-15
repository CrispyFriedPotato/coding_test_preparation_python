from sys import stdin, stdout

n = int(stdin.readline())
numbers = []

for i in range(n):
    numbers.append(int(stdin.readline()))
    
# for i in sys.stdin:
#     numbers.append(int(i))
numbers.sort()

# for j in numbers:
    # print(j)

stdout.write('\n'.join(map(str,numbers)))