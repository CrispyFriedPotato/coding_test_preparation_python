m = int(input())
n = int(input())

total_prime = 0
min_prime = 10001

# 소수라고 초기화
primes = [True] * (n-m+1)

for num in range(m,n+1):
    if num == 1:
        primes[num-m] = False
        continue
    for i in range(2,int(num**(1/2))+1):
        if num % i == 0:
            primes[num-m] = False
            break
for i in range(len(primes)):
    if primes[i] == True:
        if min_prime > (i+m):
            min_prime = i+m
        prime = i + m 
        total_prime += prime

# print(primes)///
if True not in primes: # if there is no prime number.
    print(-1)        
else: # There is more than one prime number.
    print(total_prime)
    print(min_prime)