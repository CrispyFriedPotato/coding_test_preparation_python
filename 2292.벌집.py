sum = 1
n = int(input())
i = 1

while True:
    if n == 1:  
        print(1)
        break
    sum += 6*i
    if n <= sum :
        print(i+1)
        break
    i += 1