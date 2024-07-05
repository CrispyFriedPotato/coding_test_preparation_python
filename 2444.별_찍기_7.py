a = int(input())

for i in range(a-1):
    for j in range(a-1-i):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    # for j in range(a-1-i):
    #     print(' ',end='')
    print()
for i in range(a-1,-1,-1):
    for j in range(a-1-i,0,-1):
        print(' ',end='')
    for j in range(2*i+1,0,-1):
        print('*',end='')
    # for j in range(a-1-i,0,-1):
    #     print(' ',end='')
    print()        