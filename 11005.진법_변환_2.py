chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number, b = input().split()

answer = ''
share = int(number)

while share:
    remainder = share % int(b)
    answer = chars[remainder] + answer
    share = share // int(b)
    
    
print(answer)