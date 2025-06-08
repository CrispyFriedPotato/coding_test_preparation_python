import sys

n, m = map(int,input().split())
x, y, direc = map(int, input().split())
maps  = [[map(int,line.split())] for line in sys.stdin.read().splitlines()]
count = 0

####answer sheet####
# n, m = map(int, input().split())

# d = [[0] * m for _ in range(n)]
# x, y, direction = map(int, input().split())
# d[x][y] = 1

# array = []
# for i in range(n):
#     array.append(list(map(int,input().split())))
    

# dx = [-1, 0, 1, 0] # North, East, South, West
# dy = [0, 1, 0, -1]

# def turn_left():
#     global direction
#     direction -=1
#     if direction == -1:
#         direction = 3

# # start simulation

# count = 1
# turn_time = 0
# while True:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
    
#     # After turning, if there is not  visited place
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
    
#     else: # After turning, all visited place or sea
#         turn_time -=1
    
#     # four direction unavailable
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
        
#         # If Back available
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
            
#         # If back is sea
#         else:
#             break
#         turn_time = 0
    
# print(count)