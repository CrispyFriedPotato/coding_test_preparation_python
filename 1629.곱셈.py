import sys


def pow(a,b,c):
    if b == 1 : 
        return a % c

    val = pow(a, b//2, c)
    val = val * val % c
    if (b % 2 == 0): 
        return val
    return val * a % c

a, b, c = map(int, sys.stdin.readline().split())
print(pow(a,b,c))


# 1% 시간초과, 숫자가 매우 큼
# rem = a % c 
# if a > c:
#     rem = (rem**2) % c
#     for i in range(3,b+1):
#         rem = rem % c
# else:
#     rem = (rem % c) ** 2
#     for i in range(2, b+1):
#         rem = rem % c

# print(rem)
