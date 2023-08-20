from collections import deque
n = int(input())
data = [input() for _ in range(n)]
move = [(0,1), (0,-1), (1,0), (-1,0)]

def solve(y,x,color,visit):
    visit[y][x] = True
    q = deque()
    q.append([y,x,color])
    while q:
        y,x,color = q.popleft()
        for i,j in move:
            if 0 <= y+i < n and 0 <= x+j <n and visit[y+i][x+j] == False and (color == data[y+i][x+j] or (color == 'R' or color == 'G') and (data[y+i][x+j] == 'R'or data[y+i][x+j] == 'G')): 
                q.append([y+i,x+j,data[y+i][x+j]])
                visit[y+i][x+j] = True
    return visit

def solve2(y,x,color, visit):
    q = deque()
    q.append([y,x,color])
    while q:
        y,x,color = q.popleft()
        for i,j in move:
            if 0 <= y+i < n and 0 <= x+j <n and visit[y+i][x+j] == False and (color == data[y+i][x+j]): 
                q.append([y+i,x+j,data[y+i][x+j]])
                visit[y+i][x+j] = True
    return visit




visit = [[False] * n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            visit[i][j] = True
            visit = solve2(i,j,data[i][j],visit)
            answer += 1
print(answer , end= ' ')


visit = [[False for _ in range(n)]  for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:

            solve(i,j,data[i][j],visit)
            answer += 1
print(answer , end= ' ')
