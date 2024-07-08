import sys


for i in sys.stdin:
    a, b = map(int,i.split())
    neither = 0
    if a==b:
        break
    elif a>b:
        if a%b == 0:
            print("multiple")
            neither = 1     
    else:
        for j in range(2,int(b*(1/2))+1):
            if a % j == 0:
                print("factor")
                neither = 1
                break
  
    if neither == 0:
        print("neither")
    