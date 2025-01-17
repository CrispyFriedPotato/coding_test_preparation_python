import sys

row, col = map(int, sys.stdin.readline().split())
chess = list(map(list,sys.stdin.read().splitlines()))

min_error = 2500 # 50x50 다 수정해야하는 경우

num_correct_start_W = 0 #start가 white인 경우
num_correct_start_B = 0 #start가 black인 경우

if row==8 and col==8:
    start = chess[0][0] 
    if start == 'W':
        for i in range(0,row,2):
            for j in range(0,col,2):
                if chess[i][j] != start: # start와 같지 않으면
                    num_correct_start_W += 1
            for j in range(1,col,2):
                if chess[i][j] == start: # start와 달라야하지만 같은 경우
                    num_correct_start_W += 1
        for i in range(1,row,2):
            for j in range(0,col,2):
                if chess[i][j] == start: # 다음 줄. start와 같으면면
                    num_correct_start_W += 1
            for j in range(1,col,2):
                if chess[i][j] != start: # start와 같아야하지만 다른 경우
                    num_correct_start_W += 1
        start = 'B' # start가 W인데 start를 B로 바꾼다면?
        for i in range(0,row,2): 
            for j in range(0,col,2):
                if chess[i][j] != start: # start와 같지 않으면
                    num_correct_start_B += 1
            for j in range(1,col,2):
                if chess[i][j] == start: # start와 달라야하지만 같은 경우
                    num_correct_start_B += 1
        for i in range(1,row,2):
            for j in range(0,col,2):
                if chess[i][j] == start: # 다음 줄. start와 같으면면
                    num_correct_start_B += 1
            for j in range(1,col,2):
                if chess[i][j] != start: # start와 같아야하지만 다른 경우
                    num_correct_start_B += 1   
    else:
        for i in range(0,row,2):
            for j in range(0,col,2):
                if chess[i][j] != start: # start와 같지 않으면
                    num_correct_start_B += 1
            for j in range(1,col,2):
                if chess[i][j] == start: # start와 달라야하지만 같은 경우
                    num_correct_start_B += 1
        for i in range(1,row,2):
            for j in range(0,col,2):
                if chess[i][j] == start: # 다음 줄. start와 같으면면
                    num_correct_start_B += 1
            for j in range(1,col,2):
                if chess[i][j] != start: # start와 같아야하지만 다른 경우
                    num_correct_start_B += 1
        start = 'W' # start가 B인데 start를 W로 바꾼다면?
        for i in range(0,row,2):
            for j in range(0,col,2):
                if chess[i][j] != start: # start와 같지 않으면
                    num_correct_start_W += 1
            for j in range(1,col,2):
                if chess[i][j] == start: # start와 달라야하지만 같은 경우
                    num_correct_start_W += 1
        for i in range(1,row,2):
            for j in range(0,col,2):
                if chess[i][j] == start: # 다음 줄. start와 같으면면
                    num_correct_start_W += 1
            for j in range(1,col,2):
                if chess[i][j] != start: # start와 같아야하지만 다른 경우
                    num_correct_start_W += 1
            
    if min_error > num_correct_start_B:
        min_error = num_correct_start_B
    if min_error > num_correct_start_W:
        min_error = num_correct_start_W
        
        
for r in range(row-7):
    for c in range(col-7):
        start = chess[r][c] 
        if start == 'W':
            for i in range(r,r+8,2):
                for j in range(c,c+8,2):
                    if chess[i][j] != start: # start와 같지 않으면
                        num_correct_start_W += 1
                for j in range(c+1,c+8,2):
                    if chess[i][j] == start: # start와 달라야하지만 같은 경우
                        num_correct_start_W += 1
            for i in range(r+1,r+8,2):
                for j in range(c,c+8,2):
                    if chess[i][j] == start: # 다음 줄. start와 같으면면
                        num_correct_start_W += 1
                for j in range(c+1,c+8,2):
                    if chess[i][j] != start: # start와 같아야하지만 다른 경우
                        num_correct_start_W += 1
            start = 'B' # start가 W인데 start를 B로 바꾼다면?
            for i in range(r,r+8,2): 
                for j in range(c,c+8,2):
                    if chess[i][j] != start: # start와 같지 않으면
                        num_correct_start_B += 1
                for j in range(c+1,c+8,2):
                    if chess[i][j] == start: # start와 달라야하지만 같은 경우
                        num_correct_start_B += 1
            for i in range(r+1,r+8,2):
                for j in range(c,c+8,2):
                    if chess[i][j] == start: # 다음 줄. start와 같으면면
                        num_correct_start_B += 1
                for j in range(c+1,c+8,2):
                    if chess[i][j] != start: # start와 같아야하지만 다른 경우
                        num_correct_start_B += 1   
        else: # start가 'B'일때
            for i in range(r,r+8,2):
                for j in range(c,c+8,2):
                    if chess[i][j] != start: # start와 같지 않으면
                        num_correct_start_B += 1
                for j in range(c+1,c+8,2):
                    if chess[i][j] == start: # start와 달라야하지만 같은 경우
                        num_correct_start_B += 1
            for i in range(r+1,r+8,2):
                for j in range(c,c+8,2):
                    if chess[i][j] == start: # 다음 줄. start와 같으면
                        num_correct_start_B += 1
                for j in range(c+1,c+8,2):
                    if chess[i][j] != start: # start와 같아야하지만 다른 경우
                        num_correct_start_B += 1
            start = 'W' # start가 B인데 start를 W로 바꾼다면?
            for i in range(r,r+8,2):
                for j in range(c,c+8,2):
                    if chess[i][j] != start: # start와 같지 않으면
                        num_correct_start_W += 1
                for j in range(c+1,c+8,2):
                    if chess[i][j] == start: # start와 달라야하지만 같은 경우
                        num_correct_start_W += 1
            for i in range(r+1,r+8,2):
                for j in range(c,c+8,2):
                    if chess[i][j] == start: # 다음 줄. start와 같으면면
                        num_correct_start_W += 1
                for j in range(c+1,c+8,2):
                    if chess[i][j] != start: # start와 같아야하지만 다른 경우
                        num_correct_start_W += 1

              
        if min_error > num_correct_start_B:
            min_error = num_correct_start_B
        if min_error > num_correct_start_W:
            min_error = num_correct_start_W
        num_correct_start_B, num_correct_start_W = 0, 0

print(min_error)
                           