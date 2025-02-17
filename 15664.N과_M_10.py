import sys

def fun(k):
    if k == m:
        tmp = ''
        for i in arr:
            tmp+=(str(i)+' ')
        used.add(tmp)    
        return used
    
    for j in nums:
        if k>0 and j>=arr[k-1]:
            if issued[j]:
                arr[k] = j
                issued[j] -=1
                fun(k+1)
                issued[j] += 1
        if k == 0:
            if issued[j]:
                arr[k] = j
                issued[j] -=1
                fun(k+1)
                issued[j] += 1

n, m = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort()

used = set([])
arr = [0] * m 
issued = {i:0 for i in nums} 
for i in nums:
    issued[i]+=1
fun(0)
new = []
for i in used:
    new.append(list(map(int,i.split())))

new.sort()
for j in new:
    for k in j:
        sys.stdout.write(str(k)+' ')
    print()