price = int(input())
kinds = int(input())

price_many = []
for i in range(kinds):
    price_many.append(list(map(int,input().split())))
 
total = 0   
for i in range(kinds):
    total += (price_many[i][0]*price_many[i][1])

if price == total:
    print("Yes")
else:
    print("No")