#counting sort로 문제풀기
import sys
n = int(input())
numbers = 10001
counting_arr= [0]*numbers
# result = [0]*
for i in range(n):
    idx = int(sys.stdin.readline())
    counting_arr[idx]+=1
# numbers = list(map(int,sys.stdin.read().splitlines()))
# counting_arr = [0]*(max(numbers)+1)

# for i in range(1,n+1): # 누적합합
#     counting_arr[i] += counting_arr[i-1]
# print(counting_arr)
for idx,i in enumerate(counting_arr):
    if idx==0 or i==0:
        pass
    else:
        for j in range(i):
            print(idx)
    # val = counting_arr[i]-1
    # counting_arr[i]-=1
    # result[val] = i
# print(result)
# for i in result:
    # print(i)
