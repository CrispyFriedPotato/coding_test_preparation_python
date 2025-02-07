import sys
n = int(input())
people = []
for i in range(n):
    # people += sys.stdin.readline().split()
    people.append(sys.stdin.readline().split())
# print(people)
flag = 0
dancer = set()
before = ''
for i in people:
    if 'ChongChong' in i:
        flag = 1
        dancer.add(i[0])
        dancer.add(i[1])
    if flag == 1 and (i[0] in dancer or i[1] in dancer):
        dancer.add(i[0])
        dancer.add(i[1])
        

print(len(dancer))