n = int(input())
count = 0
if n == 0:
    print(4)
elif n == 1:
    print(9)
else:    
    for i in range(n+1):
        if i == 0:
            count +=4
        elif i == 1:
            count += 5
            x = 5
        else:
            x = 4*x - (2**(i-2))*4
            count += x
        
    print(count)       