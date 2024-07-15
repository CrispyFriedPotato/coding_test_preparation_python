import sys 

n, m = map(int, sys.stdin.readline().split())
set_n =set()
list_m = list()

for i in range(n):
    set_n.add(sys.stdin.readline().strip())

for i in range(m):
    list_m.append(sys.stdin.readline().strip())

count = 0
for i in list_m:
    if i in set_n:
        count+=1

print(count)