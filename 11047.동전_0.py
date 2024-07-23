from sys import stdin, stdout
import copy

n , k = map(int, stdin.readline().split())
coins = []
for i in range(n):
    coins.append(stdin.readline().strip())

remainder = copy.deepcopy(k)
count = 0
for i in range(n-1,-1,-1):
    if remainder // int(coins[i]) != 0:
        count += (remainder//int(coins[i]))
        remainder %= int(coins[i])

print(count)