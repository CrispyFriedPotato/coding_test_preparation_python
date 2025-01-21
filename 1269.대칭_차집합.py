import sys
_,_ = sys.stdin.readline().split()

# 시간초과
# a = list(map(int,sys.stdin.readline().split()))
# b = list(map(int,sys.stdin.readline().split()))

# 시간초과
# minus = set()
# for i in a:
#     if i not in b:
#         minus.add(i)
# for j in b:
#     if j not in a:
#         minus.add(j)

zip = {}
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
for i in a:
    zip[i] = 1
for j in b:
    if j in zip:
        del zip[j]
    else:
        zip[j] = 1
    
print(len(zip))