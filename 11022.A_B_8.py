number = int(input())
# a, b = map(int, input().split())
user_input =[]
for i in range(number):
    user_input.append(input().split())
    
for i in range(number):
    print("Case #%d: %d + %d = %d"%(i+1,int(user_input[i][0]),int(user_input[i][1]),int(user_input[i][0])+int(user_input[i][1])))