import sys

def fun(k):
    if k == m:
        for i in arr:
            sys.stdout.write(str(i)+' ')
        print()
        return
    
    for j in nums:
        if k>0 and arr[k-1] <= j:
            arr[k] = j
            fun(k+1)
            continue
        if k == 0:
            arr[k] = j
            fun(k+1)
        # if not issued[j]:
            # arr[k] = j
            # issued[j] = 1
            # fun(k+1)
            # issued[j] = 0

n, m = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort()

arr = [0] * m # 출력할 숫자 자리 수
# issued = [0] * n # 각 숫자 사용 여부
issued = {i:0 for i in nums} # 각 숫자 사용 여부
fun(0)