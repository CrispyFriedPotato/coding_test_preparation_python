import sys

n , m = map(int, input().split())
cards = [list(map(int,i.split())) for i in sys.stdin.read().splitlines()]

result = -1
for i in range(n):
    min_val = min(cards[i])
    # if max_val < min_val:
    #     max_val = min_val
    result = max(result, min_val)
print(result)