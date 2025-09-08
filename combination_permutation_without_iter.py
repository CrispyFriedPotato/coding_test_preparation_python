def permutation(path, arr, visited):
    if len(path) == 2:
        print(path)
        return
    
    for i in range(n):
        if visited[i] == True:
            continue
        visited[i] = True
        path.append(arr[i])
        permutation(path,arr, visited)
        path.pop()
        visited[i] = False


def combination(path, arr, start):
    
    if len(path) == 2:
        print(path)
        return
    
    for i in range(start,n):
        path.append(arr[i])
        combination(path,arr, i+1)
        path.pop()
    
    

n = 3
arr = [1,2,3]
visited = [False]*n
permutation([], arr,visited)
print("----------")
combination([],arr,0)