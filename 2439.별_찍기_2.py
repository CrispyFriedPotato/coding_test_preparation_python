count = int(input())

for i in range(1,count+1):
    for j in range(count-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()