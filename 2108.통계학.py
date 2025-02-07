import sys
n = int(input())

nums = list(map(int, sys.stdin.read().splitlines()))
nums.sort()
print(round(sum(nums)/n)) 
print(nums[int(n/2)])
# print(nums[round(n/2)-1]) #이게 왜 틀린가 하니 python의 round는 5미만 버리고 5 초과 올리는 시스템이다.
num_often = {i:0 for i in nums}
max_often = 0

for i in nums:
    num_often[i]+=1
for _,val in num_often.items():
    if max_often < val:
        max_often = val
time = 0
for idx,val in num_often.items():
    if val == max_often:
        time += 1
        if time == 2:
            result = idx
            break
        result = idx
        
print(result)
print(nums[n-1]-nums[0])