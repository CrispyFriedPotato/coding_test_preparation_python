import math

n = int(input())
# 약수개수가 홀수개면 창문은 열리고(1), 
# 약수개수가 짝수개면 창문은 닫힌다(0).

# 약수개수가 홀수개라는 것은 그 수는 제곱수라는 의미다.
# 따라서 log2를 해주므로써 그 전의 1 개수를 구한다.
# print(int(math.log2(n)))

print(int(math.sqrt(n)))