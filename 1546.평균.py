subj = int(input())
scores = list(map(int, input().split()))
scores.sort()

for i in range(subj):
    scores[i]=scores[i]/scores[subj-1]*100

total = 0
for i in range(subj):
    total += scores[i]
print(total/subj)