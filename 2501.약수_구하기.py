a , b = map(int,input().split())

factors = []
for i in range(1, int(a**(1/2))+1):
    if a % i == 0:
        factors.append(i)

for i in range(len(factors)-1,-1,-1):
    if a//factors[i] not in factors:
        factors.append(a//factors[i])

# print(factors)
if b > len(factors):
    print(0)
else:       
    print(factors[b-1])