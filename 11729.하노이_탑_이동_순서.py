
def Hannoi(a, b ,n):
    if n == 1: 
        print(a,b) 
        return
    Hannoi(a, 6-a-b, n-1)
    print(a,b)
    Hannoi(6-a-b, b, n-1)

n = int(input())
print(2**n-1)
Hannoi(1,3,n)
