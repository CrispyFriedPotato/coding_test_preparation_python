whole = [[0 for col in range(100)] for row in range(100)]

count = int(input())
max = 0
for i in range(count):
    col, row = map(int, input().split()) 

    for x in range(col,col+10):
        for y in range(row, row+10):
            whole[y][x] +=1
            if whole[y][x] > max:
                max = whole[y][x]

area = 0
for row in range(100):
    for col in range(100):
        if whole[row][col] != 0:
            area += 1
            
print(area)
            
    
    