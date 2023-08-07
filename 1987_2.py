r, c = map(int,input().split())
data = [input() for _ in range(r)]
move = [(0,1), (0,-1), (-1,0), (1,0)]
def dfs(now_y, now_x, cnt):
    global answer
    answer = max(answer , cnt)
    for i,j in move:
        if 0 <= now_y + i < r and 0 <= now_x + j< c:
            if not data[now_y+i][now_x+j] in visit:
                visit[data[now_y+i][now_x+j]] = 1
                dfs(now_y+i, now_x+j, cnt + 1)
                del visit[data[now_y+i][now_x + j]]
visit = dict()
visit[data[0][0]] = 1
answer = 0
dfs(0, 0, 1)
print(answer)