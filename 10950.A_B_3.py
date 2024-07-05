tc = int(input())
tc_list = []
for i in range(tc):
    tc_list.append(list(map(int,input().split())))

for i in range(tc):
    print(tc_list[i][0]+tc_list[i][1])