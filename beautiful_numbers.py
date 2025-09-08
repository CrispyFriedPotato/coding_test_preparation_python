
def isValid(path):
    count = [0 for i in range(k)]
    for i in path:
        count[i] += 1
        
    # first prunning, no remainders
    for j in range(1,k):
        if count[j] % j:
            return False
    
    i = 0
    while i < len(path):
        # second prunning, right chunks 
        if path[i] == 1:
            i +=1
            continue
        elif path[i] == 2:
            if i+1<=len(path):
                if path[i+1]==2:
                    i += 2
                else:
                    return False
            else:
                return False
        elif path[i] == 3:
            if i+2 <=len(path):
                for j in range(i,i+3):
                    if path[j] != 3:
                        return False
            else:
                    return False
            i += 3
            continue
        elif path[i] == 4:
            if i+3 <= len(path):
                for j in range(i,i+4):
                    if path[j] != 4:
                        return False
            else:
                    return False
            i += 4
            
    return True
        

def backtrack(path):
    if len(path) == n:
        if isValid(path):
            print(path)
        
        return
    for i in range(1,k):
        path.append(i)
        backtrack(path)
        path.pop()
        
        
    
    
# 1 ~ 4
k = 5
# n = int(input())
n = 3
backtrack([])