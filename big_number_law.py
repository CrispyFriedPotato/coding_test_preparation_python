n, m, k = map(int, input().split())
numbers = list(map(int,input().split()))

numbers.sort()
result = 0
for i in range(0,m,k+1):
    result += numbers[-1]*k
    result += numbers[-2]

print(result)