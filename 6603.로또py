import sys

def func(k):

    if k == 6:
        # print("here")
        for i in arr:
            sys.stdout.write(str(i) + ' ')
        print()
        return

    for i in range(n):
        if not issued[i]:
            if k>0 and numbers[i] < arr[k-1]:
                continue
            arr[k] = numbers[i]
            issued[i] = 1
            func(k+1)
            issued[i] = 0
            
            
while(True):
    lotto = sys.stdin.readline().split()
    if len(lotto) == 1:
        break
    
    n = int(lotto[0])
    numbers = list(map(int, lotto[1:]))
    arr = [0]*6
    issued = [0]*n

    func(0)
    print()
