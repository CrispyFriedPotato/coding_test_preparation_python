import sys

def sort(n):
    x, y = n.split()
    return int(y) + int(x)/1000000

sys.stdout.write(''.join(map(str,sorted(sys.stdin.readlines()[1:],key=lambda x: sort(x)))))