import sys

# 프로그래밍에서 사전순이란 문자의 아스키코드 순서라고 무방
# 0 ~ 9 : 48~57
# a ~ : 97 ~
# A ~ : 65 ~
count = int(sys.stdin.readline())
people = {}

for i in range(count):
    name, status = map(str, sys.stdin.readline().split())
    people[name] = status

who = []
for n, s in people.items():
    if s=='enter':
        who.append(n)

sys.stdout.write('\n'.join(sorted(who,reverse=True)))