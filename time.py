n = int(input())

count = 0

for hour in range(n+1):
    for minu in range(60):
        for sec in range(60):
            if '3' in str(hour)+str(minu)+str(sec):
                count += 1

print(count)