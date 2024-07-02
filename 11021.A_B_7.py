count = int(input())
plus = []
for i in range(count):
    plus.append(input().split())

for i in range(count):
    result = int(plus[i][0]) + int(plus[i][1])
    print("Case #%d: %d"%(i+1,result))