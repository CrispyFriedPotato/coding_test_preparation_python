import sys

def fun(k):
    if k == m:
        for i in arr:
            sys.stdout.write(str(i)+' ')
        print()
        return
    
    for i in range(n):
        if k == 0:
            arr[k] = i+1    
        elif k > 0 and i+1 >= arr[k-1]:
            arr[k] = i+1
        else:
            continue   
        
        fun(k+1)
        
n, m = map(int, input().split())
arr = [0]*m
fun(0)