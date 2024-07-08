import sys

square = []
for i in sys.stdin:
    square.append(list(map(int,i.split())))

col = [square[i][0] for i in range(3)]
row = [square[i][1] for i in range(3)]


# 2. 모범 답안 보고 다시 정리. count() 함수 사용하면 더 편했을것.
for i in range(3):
    if col.count(col[i]) == 1:
        dup_col = col[i]
        
    if row.count(row[i]) == 1:
        dup_row = row[i]
# 1. 안보고 푼것
# a = [col[0]]
# b = [row[0]]

# for i,j in zip(col[1:],row[1:]):  
#     if i not in a:
#         a.append(i)
#     else:
#         for k in col:
#             if i !=k:
#                 dup_col = k
#     if j not in b:
#         b.append(j)
#     else:
#         for k in row:
#             if j !=k:
#                 dup_row = k
print(dup_col,dup_row)
   