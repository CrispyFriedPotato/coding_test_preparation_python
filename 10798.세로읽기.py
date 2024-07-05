import sys

matrix = []

for i in sys.stdin:
    matrix.append(list(i.rstrip('\n')))

for j in range(15): # col
    for i in range(5): # row
        if len(matrix[i]) <= j:
            continue
        print(matrix[i][j],end="")