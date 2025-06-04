x = int(input())
food = list(map(int, input().split()))
# odd = [food[1]]
# even = [food[0]]
# for i in range(2,x): # 2, 3, 4, 5,..., x
#     if i%2 ==0:
#         even.append(even[-1]+food[i])
#     else:
#         odd.append(odd[-1]+food[i])

# print(max(odd[-1],even[-1]))


# Dynamic Programming

d = [0] * 100
d[0] = food[0]
d[1] = max(food[0],food[1])
for i in range(2,x):
    d[i] = max(d[i-1],d[i-2] + food[i])

print(d[x-1])