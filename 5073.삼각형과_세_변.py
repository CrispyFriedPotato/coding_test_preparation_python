import sys

for i in sys.stdin:
    triangle = list(map(int,i.split()))
    triangle.sort()
    if triangle[0]==triangle[1]==triangle[2]==0:
        break
    if triangle[0]+triangle[1] <= triangle[2]:
        print("Invalid")
        continue
    if triangle[0]==triangle[1]==triangle[2]:
        print("Equilateral")
        continue
    if triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[0]==triangle[2]:
        print("Isosceles")
        continue
    if triangle[0]!=triangle[1]:
        if triangle[1]!= triangle[2]:
            if triangle[0] != triangle[2]:
                print("Scalene")