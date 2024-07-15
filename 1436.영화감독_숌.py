order = int(input())

a = 0
i = 0
while(True):
    i += 1
    if '666' in str(i):
        a +=1
        if a == order:
            print(i)
            break
        