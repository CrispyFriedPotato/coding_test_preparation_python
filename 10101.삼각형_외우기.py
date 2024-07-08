a = int(input())
b = int(input())
c = int(input())


if a+b+c != 180:
    print("Error")
else:
    if a==b==c==60:
        print("Equilateral")
    if a==b:
        if b!=c:
            print("Isosceles")
    if b==c:
        if a!=b:
            print("Isosceles")
    if a==c:
        if a!=b:
            print("Isosceles")
    if a!=b:
        if b!=c and a!=c:
            print("Scalene")
        