a = input()
# 26 alphabets
aphabets = []
for i in range(26):
    aphabets.append(-1) 
for idx,i in enumerate(a):
    if aphabets[ord(i)-97] == -1:
        aphabets[ord(i)-97] = idx

for i in aphabets:
    print(i,end=" ")