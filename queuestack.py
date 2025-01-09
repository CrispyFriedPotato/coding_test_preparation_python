import sys
n = int(input()) # number of queuestack

queueStack = list(map(int, sys.stdin.readline().split()))
vals = list(map(int,sys.stdin.readline().split()))

m = int(input())
c = list(map(int,sys.stdin.readline().split()))

# 0 은 Queue, 1은 Stack
for i in c:
    x_pop = i
    pop = i
    for j in range(n):   
        if queueStack[j] == 0: #queue
            pop = vals[j] # pop
            vals[j] = x_pop #change val
        else: # stack
            x_pop = pop
    sys.stdout.write(str(pop))        
    sys.stdout.write(' ')        