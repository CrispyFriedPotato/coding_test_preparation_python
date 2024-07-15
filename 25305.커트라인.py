import sys

people, award = map(int,sys.stdin.readline().split())
scores = list(map(int,sys.stdin.readline().split()))
scores.sort()

print(scores[people-award])
# print(scores[-award])
