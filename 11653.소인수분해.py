normal = int(input())
factors = []
temp = normal
if normal == 1:
    pass
else:
    for i in range(2,10000001):
        while temp%i == 0:
            factors.append(i)
            temp /=i           
    if len(factors) == 0:
        factors.append(normal)


for i in range(len(factors)):
    print(factors[i])            