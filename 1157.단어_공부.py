a = input().lower()
freq = dict()

for i in a:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1

max = 0
max_key = ''
for key,val in freq.items():
    if val > max:
        max = val
        max_key = key

flag = 0
for i in freq.values():
    if i == max:
        flag +=1
        if flag > 1:
            max_key = "?"
print(max_key.upper())
    
