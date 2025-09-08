def rotation_clockwise(matrix):
    rotated_mat = [[row[j] for j in range(n)] for row in zip(*matrix[::-1])]    
    return rotated_mat

def rotation_anti_clockwise(matrix):
    rotated_mat = [[row[col] for row in matrix[::]] for col in range(n-1,-1,-1)]
    return rotated_mat
n = 3
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(rotation_clockwise(matrix))
print(rotation_anti_clockwise(matrix))