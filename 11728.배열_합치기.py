import sys

n , m = map(int,input().split())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

answer = []
c = a+b
c.sort()
for i in c:
    print(i, end=' ')
# def check(big_val, queue):
#     while True:
#         if not queue:
#             return
#         if big_val > queue[0]:
#             answer.append(queue[0])
#             queue.pop(0)
#         else:
#             return
            
# while True:
#     if not a or not b:
#         if a:
#             answer += a
#         else:
#             answer += b
#         break

    
#     if a[0] > b[0]:
#         check(a[0],b)
#         continue
#     if a[0] < b[0]:
#         check(b[0],a)
#         continue
#     if a[0] == b[0]:
#         answer.append(a[0])
#         a.pop(0)
#         b.pop(0)
#         continue

# for i in answer:
#  print(i,end=' ')
        