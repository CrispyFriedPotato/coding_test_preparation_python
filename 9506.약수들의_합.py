def defactorize(num):
    factors = []
    for i in range(1, int(num**(1/2)+1)):
        if num % i == 0:
            factors.append(i)

    for i in range(len(factors)-1,-1,-1):
        if num//factors[i] not in factors:
            factors.append(num//factors[i])
    
    return factors
    

while True:
    num = int(input())
    if num == -1:
        break
    factors = defactorize(num)[:-1]
    if num == sum(factors):
        answer = ' + '.join(map(str,factors))
        print(num,"=",answer)
    else:
        
        print(num,"is NOT perfect.")