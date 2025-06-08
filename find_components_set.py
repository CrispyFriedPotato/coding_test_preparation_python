# set

    
n = int(input())
n_comp = set(map(int,input().split()))
m = int(input())
m_comp = list(map(int,input().split()))

result = []

for i in m_comp:
    if i in n_comp:
        print('yes', end=' ')
    else:
        print('no', end=' ')

    