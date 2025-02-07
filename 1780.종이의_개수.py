import sys

def paper(n,numbers):
    cut = []
    result = [0,0,0]
    
    for i in range(0,n,n//3): # 9 -> 0, 3, 6, 3 -> 0 , 1, 2
        sliced = numbers[i:i+(n//3)] # [0,3][3,6][6,9], [0,1][1,2][2,3]
        for k in range(0,n,n//3): # 9 -> 0, 3, 6
            new = []
            for j in range(n//3):
                new.append(sliced[j][k:k+n//3])
            cut.append(new)
    for a in cut:
        flag = a[0][0]
        for i in a:
            for j in i:
                if j != flag:
                    flag = -2
                    break
            if flag == -2:
                break
        if flag == a[0][0]:
            idx = a[0][0]+1
            result[idx] += 1
        else:
            b = paper(n//3,a)
            for i in range(3):
                result[i]+=b[i]
    return result          
            

n = int(input())
numbers = [list(map(int,i.split())) for i in sys.stdin.read().splitlines()]
result = [0,0,0]
flag = numbers[0][0]
for i in numbers:
    for j in i:
        if flag != j:
            flag = -2
            result = paper(n,numbers)
            for i in range(3):
                print(result[i])
            break
    if flag ==-2:
        break
else:
    result[flag+1] += 1
    for i in range(3):
        print(result[i])


