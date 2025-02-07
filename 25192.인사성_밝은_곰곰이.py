import sys

n = int(input())

records = list(map(str,sys.stdin.read().splitlines()))
time = 0
people = set()

for i in records:
    if i == 'ENTER':
        time += len(people)
        people = set()
        
    else:
        people.add(i)
time += len(people)        
print(time)