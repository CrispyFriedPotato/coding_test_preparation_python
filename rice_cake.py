n, m = map(int, input().split())
length = list(map(int, input().split()))

max_rice = max(length)
min_rice = min(length)
result = 0

def binary_search(data, target, start, end):
    if start > end:
        print(start, end)
        return None
    
    mid = (end+start)//2
    left_rice = []
    for i in range(n):
        val = data[i]-mid
        if val < 0:
            left_rice.append(0)
        else:
            left_rice.append(val)
    
    total = sum(left_rice)

    if target > total:
        return binary_search(length, m,  min_rice, mid+1)
    elif target < total :
        return binary_search(length, m, mid-1, max_rice)     
    else:
        return mid
    
        
print(binary_search(length, m, min_rice, max_rice))

    