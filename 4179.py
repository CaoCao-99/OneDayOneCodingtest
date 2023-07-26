from collections import deque
r,c = map(int,input().split())
move = [(-1,0), (1,0), (0,1), (0,-1)]
data = [input() for _ in range(r)]
for i in range(r):
    for j in range(c):
        if data[i][j] == 'J':
            h_y, h_x = i,j
        if data[i][j] == 'F':
            f_y, f_x = i,j
    
q = deque()
fire_q = deque()
q.append([h_y,h_x,1])
fire_q.appendleft([f_y, f_x,1])
now_cnt = 0


while q:
    now_cnt+=1
    while fire_q:
        y_1, x_1, cnt_1 = fire_q.popleft()
        if now_cnt == cnt_1:
            for i,j in move:
                if 0 <= y_1 + i < r and 0 <= x_1+ j < c and (data[y_1+i][x_1+j] == '.' or data[y_1+i][x_1+j] == 'H'):
                    new_data = list(data[y_1+i])
                    new_data[x_1+j] = 'F'
                    data[y_1+i] = ''.join(new_data)
                    fire_q.append([y_1+i, x_1+j, cnt_1 + 1])
        else:
            fire_q.appendleft([y_1,x_1,cnt_1])
            break





    y,x,cnt = q.popleft()
    
    if y == 0 or y == r-1 or x == 0 or x == c-1:
        print(cnt)
        exit()
    if now_cnt == cnt:
        for i,j in move:
            if 0 <= y + i < r and 0 <= x + j < c and data[y+i][x+j] == '.':
                new_data = list(data[y+i])
                new_data[x+j] = 'H'
                data[y+i] = ''.join(new_data)
                q.append([y+i, x+j, cnt+1])
    else:
        q.appendleft([y,x,cnt])
        break
print("IMPOSSIBLE")

