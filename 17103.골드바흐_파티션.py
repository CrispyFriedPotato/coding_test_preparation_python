import sys

def eratos(n):
    arr = [i for i in range(n)]
    mid = int(n*(1/2))
    for i in range(2,mid+1):
        if arr[i] == 0:
            continue
        for j in range(i*i,n,i):
            arr[j] = 0
    arr[1]=0
    return arr

def gold_bach(arr,n):
    partition_number = 0
    for i in range(int(n/2)+1):
        if i == 0 or i == 1:
            continue
        if arr[i]:
            if arr[n-i] and i<=(n-i):
                partition_number += 1
    print(partition_number)
        
    
        
T = int(input()) # number of test case
tc = list(map(int,sys.stdin.read().splitlines())) # test case, even numbers

max_num = 1000001
eratos_list = eratos(max_num)
for i in tc:
    gold_bach(eratos_list, i)
