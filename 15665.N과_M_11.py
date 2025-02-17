import sys

def fun(k):
    if k == m:
        tmp = ''
        for i in arr:
            tmp+=(str(i)+' ')
        used.add(tmp)    
        return used
    
    for j in nums:
            arr[k] = j
            fun(k+1)
        

n, m = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort()

used = set([])
arr = [0] * m 
fun(0)
new = []
for i in used:
    new.append(list(map(int,i.split())))

new.sort()
for j in new:
    for k in j:
        sys.stdout.write(str(k)+' ')
    print()