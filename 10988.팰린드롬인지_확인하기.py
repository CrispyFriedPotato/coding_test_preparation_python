a = input()

for i in range(len(a)):
    if a[i] != a[len(a)-(i+1)]:
        print(0)
        break
    if i == len(a)-1:
        print(1)    