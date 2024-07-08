import sys
n = int(input())
coin = [25,10,5,1]
for line in sys.stdin:
    money = int(line.rstrip('\n'))
    answer = ''
    
    for i in range(4):
        answer += str(money//coin[i]) 
        answer += ' '
        money -= money//coin[i] * coin[i]
    print(answer)
    
