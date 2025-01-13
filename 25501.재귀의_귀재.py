import sys 

def recursion(count, s, l, r):
    count += 1
    if l >= r: return str(1)+' '+str(count)
    elif s[l] != s[r]: return str(0)+' '+str(count)
    else: return recursion(count, s, l+1, r-1)

def isPalindrome(s, count):
    return recursion(count, s, 0, len(s)-1)


_ = int(input())
S = sys.stdin.read().splitlines()

for i in S:
    count = 0
    print(isPalindrome(i, count))
