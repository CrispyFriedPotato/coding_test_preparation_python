import sys

def func(k):
    mo = ['a','e','i','o','u']
    
    if k == n:
        mo_count = 0
        for i in arr:
            if i in mo:
                mo_count +=1
        if mo_count <1:
            return
        if n - mo_count <2:
            return
        for i in arr:
            sys.stdout.write(i)
        print()
        
        return
    
    for i in range(m):
        if not issued[i]:
            if k>0 and arr[k-1]>letters[i]:
                continue
            arr[k] = letters[i]
            issued[i] = 1
            func(k+1)
            issued[i] = 0
        

n, m = map(int, sys.stdin.readline().split())

letters = sys.stdin.readline().split()
letters.sort()

arr = [''] * n
issued = [0] * m
func(0)
