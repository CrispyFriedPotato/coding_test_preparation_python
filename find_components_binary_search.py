# binary_search

def binary_search(array,target,start,end):
    if start > end:
        return None
    
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array,target, mid+1, end)
    else:
        return binary_search(array,target, start, mid-1)
    
n = int(input())
n_comp = list(map(int,input().split()))
m = int(input())
m_comp = list(map(int,input().split()))

n_comp.sort()
result = []

for i in m_comp:
    result.append(binary_search(n_comp, i, 0, n))
    
for i in result:
    if i == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
    