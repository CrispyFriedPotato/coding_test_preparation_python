import sys

matrix = []
for i in sys.stdin:
    matrix.append(list(map(int, i.split())))

max = -1
row=-1
col =-1
for i in range(9):
    for j in range(9):
       if matrix[i][j] > max: 
           row = i
           col = j
           max = matrix[i][j]

print(max)
print(row+1, col+1)