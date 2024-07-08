import sys

count = int(input())
lands = []
for i in sys.stdin:
    lands.append(list(map(int,i.split())))

min_x = 10000
max_x = -10000
min_y = 10000
max_y = -10000

x = [lands[i][0] for i in range(len(lands))]
y = [lands[i][1] for i in range(len(lands))]

for i,j in zip(x,y):
    if min_x > i:
        min_x = i
    if max_x < i:
        max_x = i
    if min_y > j:
        min_y = j
    if max_y < j:
        max_y = j

print((max_x-min_x)*(max_y-min_y))
