scores = list(map(int,input().split()))
scores.sort()
if scores[0] == scores[1]:
    if scores[1] == scores[2]: # 3개가 같은 경우
        print(10000 + scores[0]*1000)
    else: # [0]과 [1],2개만 같은 경우
        print(1000 + scores[0]*100)
elif scores[1] == scores[2]: # [1]과 [2], 2개만 같은 경우
    print(1000 + scores[2]*100)
else:
    print(scores[2]*100)