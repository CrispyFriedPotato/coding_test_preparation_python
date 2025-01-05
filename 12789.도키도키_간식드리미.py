import sys

def sol():
    people = int(sys.stdin.readline())
    orders = list(map(int,sys.stdin.readline().split()))

    count = 1
    i = 0
    stack = []
    while i<len(orders):
        if orders[i] == count:
            count += 1
            i += 1
        else:
            if stack and stack[-1] == count:
                stack.pop()
                count += 1
            else:
                stack.append(orders[i])
                i += 1

    while stack:
        if stack[-1] == count:
            stack.pop()
            count+=1
        else:
            return(print("Sad"))
    else:
        return(print("Nice"))

sol()