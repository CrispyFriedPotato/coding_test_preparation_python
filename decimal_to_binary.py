# 10진수를 입력받아 2진수로 변환해 반환하는 solution( ) 함수를 구현하세요.

def solution(dec):
    an = []
    while True:
        an.append(dec % 2)  
        dec = dec//2
        if dec == 1:
            an.append(dec)
            break
    print(an[::-1])
    return an[::-1]

print(solution(12))
print(solution(10))
print(solution(2))