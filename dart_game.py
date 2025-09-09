def solution(dartResult):
    scores = ["0","1","2","3","4","5","6","7","8","9","10"]
    bonus = ["S","D","T"]
    options = ["*","#"]
    num = -100
    num_flag = 0
    answer = []
    for ch in dartResult:
        if ch in scores:
            if num_flag == 1:
                answer[-1] = 10
                num_flag = 0
                continue
            num = int(ch)
            answer.append(num)
            num_flag = 1
        if ch in bonus:
            num_flag = 0
            if ch =="S":
                answer[-1] = answer[-1]
            elif ch == "D":
                answer[-1] = answer[-1]**2
            else:
                answer[-1] = answer[-1]**3
        
        if ch in options:
            num_flag = 0
            if ch == "*":
                if len(answer) == 1:
                    answer[-1] *= 2
                else:
                    answer[-1] *= 2
                    answer[-2] *= 2
            else:
                answer[-1] *= -1
                    
        
    
    return sum(answer)