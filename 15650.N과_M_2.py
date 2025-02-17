import sys

def func(k):
    if k == m:
        for i in arr:
            sys.stdout.write(str(i)+' ')
        print()
        return
    
    for i in range(0,n): # 0 ~ (n-1)
        if k>=1 and arr[k-1] > i+1:
            continue
        if not issued[i]:
            issued[i] = 1
            arr[k] = i+1   
            func(k+1)
            issued[i] = 0
        
     
n, m = map(int,input().split())
arr = [0]*m
issued = [0]*n
func(0)