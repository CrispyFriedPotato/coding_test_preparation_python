import sys

total_credit = 0.0
total_score = 0.0
score_base = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,
              'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
for i in sys.stdin:
    sbj, credit, score = i.split()
    if score == 'P' :
        continue
    total_credit += float(credit)
    total_score += float(credit)*float(score_base[score])

print(total_score/total_credit)