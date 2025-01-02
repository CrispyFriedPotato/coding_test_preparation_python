# by 저자. 08 괄호 짝 맞추기
# 소괄호는 짝을 맞춘 열린 괄호 ‘(’와 닫힌 괄호 ‘)’로 구성합니다. 
# 문제에서는 열린 괄호나 닫힌 괄호가 마구 뒤섞인 문자열을 줍니다. 
# 이때 소괄호가 정상으로 열고 닫혔는지 판별하는 solution( ) 함수를 구현하세요. 
# 만약 소괄호가 정상적으로 열고 닫혔다면 True를, 그렇지 않다면 False를 반환하면 됩니다.

def solution(bracket):
    
    # 아래 코드는 안되는 이유: 
    # 예를 들어 ')(' 이런 문자열이 들어온경우에, 짝이 맞지 않음에도 갯수만 보고 True라고 함함
    # open = bracket.count('(')
    # close = bracket.count(')')
    # if open == close:
    #     return True
    # else:
    #     return False
    
    a = []
    # top = -1
    for i in range(len(bracket)):
        if bracket[i] == '(':
            a.append(bracket[i])
            # top += 1
        else:
            if len(a) != 0:
                a.pop()
            else:
                return False
    if len(a) == 0:
        return True
    else:
        return False
                

print(solution('(())()'))
print(solution('((())()'))