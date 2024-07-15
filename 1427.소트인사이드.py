import sys

# 1. Jiho's First Answer
# numbers = list(map(str,sys.stdin.readline().rstrip()))
# numbers.sort(reverse=True)
# sys.stdout.write(''.join(map(str,numbers)))

# 2. Other Anser
print(*sorted(sys.stdin.readline(),reverse=True),sep="")
