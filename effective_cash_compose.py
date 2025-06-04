n, m = map(int,input().split())
money = []
for i in range(n):
    money.append(int(input()))

d = [10001]*(m+1)
d[0] = 0
for i in money:
    d[i] = 1

min_val = min(money)

for i in range(min_val,m+1):
    for j in money:
        d[i] = min(d[i-j]+1,d[i])
    
print( -1 if d[m]==101 else d[m])


# Answer Sheet
# for i in range(n):
#     for j in range(money[i], m+1):
#         if d[j-money[i]] != 10001:
#             d[j] = min(d[j], d[j-array[i]]+1)