import sys

students = []
bad_stdnts = []
for i in range(1,29):
    students.append(int(input()))

for i in range(1,31):
    if i not in students:
        bad_stdnts.append(i)

print(bad_stdnts[0])
print(bad_stdnts[1])
    

                