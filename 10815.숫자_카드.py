from sys import stdin, stdout

n = int(stdin.readline().strip())
cards = set(map(int, stdin.readline().split()))
m = int(stdin.readline().strip())
cards_sang = list(map(int, stdin.readline().split()))
# print(cards)
for i in cards_sang:
    if i in cards:
        print(1,end=" ")
    else:
        print(0,end=" ")