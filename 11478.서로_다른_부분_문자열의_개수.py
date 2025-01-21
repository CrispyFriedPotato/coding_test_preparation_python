n = input()
n_len = len(n)

result = set()
for j in range(1,n_len+1):
    for i in range(0,n_len):
        result.add(n[i:i+j])
print(len(result))
        