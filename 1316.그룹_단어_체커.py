count = int(input())

group_word = 0

# 뛰어져 있는 중에 앞에 같은 알파벳이 있으면 안됨

for i in range(count):
    word = input()
    flag = 1
    for j in range(1,len(word)):
        if word[j] !=word[j-1]:
            if word[j] in word[:j-1]:
                flag = 0
    if flag != 0:
        group_word +=1

print(group_word)
            