# 게임 이론의 경우 이렇게 규칙을 찾아서 하는 경우 또는 DP로 푸는 경우가 있따.

n = int(input())

# 1 . DP로 풀기 - 블로그 참조함
D = [0]*1001
D[1] = 1
D[2] = 2
D[3] = 1

for i in range(4,n+1):
    D[i] = min(D[i-1],D[i-3]) + 1

if D[n]%2==0:
    print("CY")
else:
    print("SK")
    
# 2. 규칙
# if n%2==0:
#     print('CY')
# else:
#     print('SK')

