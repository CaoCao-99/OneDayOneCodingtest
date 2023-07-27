from collections import deque
r,c = map(int,input().split())
move = [(-1,0), (1,0), (0,1), (0,-1)]
data = [input() for _ in range(r)]
f_visit = [[100000000 for _ in range(c)]for _ in range(r)]
j_visit = [[-1 for _ in range(c)]for _ in range(r)]
q = deque()
fire_q = deque()
for i in range(r):
    for j in range(c):
        if data[i][j] == 'J':
            q.append([i,j])
            j_visit[i][j] = 1
        if data[i][j] == 'F':
            fire_q.append([i,j])
            f_visit[i][j] = 1
    



while fire_q:
    y_1, x_1 = fire_q.popleft()
    for i,j in move:
        if 0 <= y_1 + i < r and 0 <= x_1+ j < c and f_visit[y_1+i][x_1+j] == 100000000 and data[y_1+i][x_1+j] != '#':
            f_visit[y_1+i][x_1+j] = f_visit[y_1][x_1] + 1
            fire_q.append([y_1+i, x_1+j])



while q:
    y,x = q.popleft()
    if y == 0 or y == r-1 or x == 0 or x == c-1:
        print(j_visit[y][x])
        exit()

    for i,j in move:
        if 0 <= y + i < r and 0 <= x + j < c and j_visit[y+i][x+j] == -1 and data[y+i][x+j] == '.' and f_visit[y+i][x+j] > j_visit[y][x] + 1:
            j_visit[y+i][x+j] = j_visit[y][x] + 1
            q.append([y+i, x+j])


print("IMPOSSIBLE")