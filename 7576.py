from collections import deque
c, r = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(r)]
q = deque()
move = [(0,1), (0,-1), (1,0), (-1,0)]
for i in range(r):
    for j in range(c):
        if data[i][j] == 1:
           q.append([i,j])
answer = 1
while q:
    y,x = q.popleft()
    for i, j in move:
        if 0 <= y+i < r and 0 <= x+j < c and data[y+i][x+j] == 0:
            data[y+i][x+j] = data[y][x] + 1
            answer = max(answer, data[y+i][x+j])
            q.append([y+i,x+j])
for i in range(r):
    for j in range(c):
        if data[i][j] == 0:
            print(-1)
            exit()

print(answer-1)
