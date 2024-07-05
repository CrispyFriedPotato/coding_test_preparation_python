original = [1,1,2,2,2,8]
piecies = list(map(int, input().split()))

for i in range(len(original)):
    piecies[i] = original[i]-piecies[i]
    print(piecies[i],end=' ')