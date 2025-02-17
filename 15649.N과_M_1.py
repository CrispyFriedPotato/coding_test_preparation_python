import sys

def func(k):
    if k == m:
        for i in arr:
            sys.stdout.write(str(i)+' ')
        print()
        return
    
    for i in range(0,n):
        if not issued[i] :
            issued[i] = 1
            arr[k] = i+1
            func(k+1)
            issued[i] = 0
        else:
            continue
     
n, m = map(int,input().split())
arr = [0]*m
issued = [0]*n
func(0)