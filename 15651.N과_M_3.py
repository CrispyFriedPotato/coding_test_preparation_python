import sys

def fun(k):
    if k == m:
        for j in arr:
            sys.stdout.write(str(j)+' ')
        print()
        return
    
    for i in range(n):
        arr[k] = i+1
        fun(k+1)
        
    
    
        
    
    
n, m = map(int, input().split())
arr = [0]*m # m의 자리 숫자
fun(0)
# issued = [0]*n # 1~n까지의 숫자 사용
