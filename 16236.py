from collections import deque
import copy
n = int(input())
move = [(0,1), (0,-1), (-1,0), (1,0)]
data = [list(map(int,input().split())) for _ in range(n)]
visit = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            s_y, s_x, s_size = i,j,2#이동 좌표, 현재 물고기 사이즈
            visit[i][j] = 0








def search(y,x,size, visit, data):
    new_visit = [[-1] * n for _ in range(n)]
    new_visit[y][x] = visit[y][x]
    new_data = copy.deepcopy(data)
    q=deque()
    q.append([y,x,size])
    answer = []
    while q:
        now_y,now_x,now_size = q.popleft()
        for i,j in move:
            if  0 <= now_y+i < n and 0 <= now_x+j < n and new_visit[now_y+i][now_x+j] == -1 and now_size >= new_data[now_y+i][now_x+j]:
                if new_data[now_y+i][now_x+j] == 0 or new_data[now_y+i][now_x+j] == int(now_size):
                    new_visit[now_y+i][now_x+j] = new_visit[now_y][now_x]+1
                    q.append([now_y + i, now_x+j, now_size])
                else:
                    new_visit[now_y+i][now_x+j] = new_visit[now_y][now_x]+1
                    answer.append([new_visit[now_y+i][now_x+j], now_y + i, now_x+j, now_size + 1 / int(now_size)])
    if answer:
        f = sorted(answer, key = lambda x : (x[0], x[1], x[2])) # 걸린 시간, y,x, 크기
        a,b,c,d = f[0]
        visit[b][c] = a
        data[b][c] = 0
        return search(b,c,d,visit,data)
    else:
        return new_visit[y][x]#걸린 시간 
    
    



print(search(s_y,s_x,s_size,visit,data))
