# 왕실의 나이트
loc = input()
dic_y = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

y, x = int(dic_y[loc[0]]), int(loc[1])

move_x = [2,2,-2,-2,1,-1,1,-1] # 수직
move_y = [1,-1,1,-1,2,2,-2,-2] # 수평


count = 0

for i in range(8):
    nx = x + move_x[i]
    ny = y + move_y[i]
    
    if 1<=nx<=8 and 1<=ny<=8:
        count += 1

print(count)
