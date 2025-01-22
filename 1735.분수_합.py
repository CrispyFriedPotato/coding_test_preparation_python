# import sys

# za1, mo1 = map(int, input().split())
# za2, mo2 = map(int, input().split())

# if mo1%mo2==0 or mo2%mo1==0:
#     if mo1>mo2:
#         temp = mo1//mo2
#         za = za1+(za2*temp)
#         mo = mo1
#     else:
#         temp = mo2//mo1
#         za = za2 + (za1*temp)
#         mo = mo2       
# else:
#     za = za1*mo2+za2*mo1
#     mo = mo1*mo2


# for i in range(2,30001):
#     while mo%i==0 and za%i==0:
#         mo //= i
#         za //= i


# sys.stdout.write(str(za)+' '+str(mo))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a,b = map(int,input().split())
x,y = map(int,input().split())

p = a*y + b*x
q = b*y

g = gcd(p,q)
print(p//g, q//g)