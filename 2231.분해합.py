str_n = str(input())
int_n = int(str_n)

length = len(str_n)
if length == 1:
    if int_n % 2 == 0:
        print(int_n // 2)
    else:
        print(0)
else:
    minim = (10**(length-1))//10
    for i in range(minim, int_n):
        str_minim = list(map(int,str(i)))
        if i + sum(str_minim) == int_n:
            print(i)
            break
    else:
        print(0)
    
