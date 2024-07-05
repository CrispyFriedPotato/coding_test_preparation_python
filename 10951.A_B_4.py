import sys

while True:
    a = sys.stdin.readline()
    if a == '\n' or a=='':
        break
    else:
        a = list(map(int,a.split()))
        print(a[0]+a[1])