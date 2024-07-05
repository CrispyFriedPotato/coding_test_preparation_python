a = input()
total = 0
for i in a:
    if ord(i)%65 <3:
        total += 3
    elif 3 <= ord(i)%65 and ord(i)%65<6:
        total += 4         
    elif 6 <= ord(i)%65 and ord(i)%65<9:
        total += 5
    elif 9 <= ord(i)%65 and ord(i)%65<12:
        total += 6
    elif 12 <= ord(i)%65 and ord(i)%65<15:
        total += 7
    elif 15 <= ord(i)%65 and ord(i)%65<19:
        total += 8
    elif 19 <= ord(i)%65 and ord(i)%65<22:
        total += 9
    elif 22 <= ord(i)%65 and ord(i)%65<26:
        total += 10
    
print(total)