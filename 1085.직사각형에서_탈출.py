x, y, w, h = map(int, input().split())


a=0
b=0

if w/2 > x :
    a = x
else:
    a = w-x

if h/2 > y:
    b = y
else:
    b  = h-y

if a>=b:
    print(b)
else:
    print(a)