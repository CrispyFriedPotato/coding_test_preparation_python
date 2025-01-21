import sys
n, m = map(int,sys.stdin.readline().split())
nev_heard = {}
nev_heard_seen = []
count = 0


for i in range(n):
    nev_heard[sys.stdin.readline().split()[0]] = 1
for i in range(m):
    j = sys.stdin.readline().split()[0]
    if nev_heard.get(j,0):
        count+=1
        nev_heard_seen.append(j)

print(count)
nev_heard_seen.sort()            #O(nlogn)
for i in nev_heard_seen:
    sys.stdout.write(i+'\n')
            