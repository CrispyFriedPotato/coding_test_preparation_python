#up_down_left_right
n = int(input())
order = list(input().split())

loc = [1, 1]

for dir in order:
    if dir == 'R':
       if loc[1] + 1 <= n: 
           loc[1] += 1
    elif dir == 'L':
        if loc[1] - 1 >= 1:
            loc[1] -= 1
    elif dir == 'U':
        if loc[0]-1 >=1:
            loc[0] -=1
    elif dir == 'D':
        if loc[0]+1<=n:
            loc[0] +=1
            
print(loc[0],loc[1])