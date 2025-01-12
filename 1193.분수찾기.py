# 1+2+3+4+5+.../+n = n(n+1)/2 = x

count = 1
sum = 0
x = int(input())
while sum < x:
    if x <= sum + count:
        t = x-sum
        if count%2 == 0:
            print(str(t)+'/'+str(count+1-t))
        else:
            print(str(count+1-t)+'/'+str(t))
        break
    else:
        sum += count
        count += 1
    
count -=1