bowls = input() # input이 띄어쓰기로 입력되지 않음. so split()이 소용이 없음.
height = 0

for i,_ in enumerate(bowls):
    if i == 0:
        height += 10
    else:
        if bowls[i-1] != bowls[i]:
            height += 10
        else:
            height +=5
            
print(height)    
    
