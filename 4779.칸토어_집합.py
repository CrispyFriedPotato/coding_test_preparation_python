import sys
# sys.setrecursionlimit(10000)

def cut(A, p, q):
    if (q-p) == 1:
        return
    start = (q-p)//3 + p
    end = q - (q-p)//3
    A[start:end] = [' ']*(end-start)
    # print(A)
    cut(A,p,start)
    cut(A,end,q)

ns = sys.stdin.read().splitlines()
for i in ns:
    lines = ['-']*(3**int(i))
    cut(lines, 0,3**int(i))
    
    for i in lines:
        sys.stdout.write(i)
    print()