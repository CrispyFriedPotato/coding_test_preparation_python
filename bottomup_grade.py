n = int(input())
name_grade = []
for _ in range(n):
    input_data = input().split()
    name_grade.append((input_data[0],input_data[1]))

name_grade.sort(key=lambda student:student[1])

for i in name_grade:
    print(i[0], end= ' ')