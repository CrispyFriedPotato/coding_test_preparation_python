num_cards, m = map(int,input().split())
cards = list(map(int,input().split()))

max = -1 # max 이면서도 m을 넘지 않는 수를 찾아야한다.
cards.sort()
for i in range(num_cards-2):
    total = 0
    for j in range(i+1,num_cards-1):
        for k in range(j+1,num_cards):
            total = cards[i] + cards[j] + cards[k]
            
            if max < total and total <= m:
                max = total

print(max)