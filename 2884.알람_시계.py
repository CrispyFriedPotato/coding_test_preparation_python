time = list(map(int,input().split()))

if time[1]>=45:
    time[1]-=45
else:
    if time[0]!=0:
        time[0]-=1
    else:
        time[0] = 23
    time[1]+=15
print(time[0],time[1])