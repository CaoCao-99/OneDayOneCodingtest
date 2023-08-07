r, c = map(int,input().split())
data = [input() for _ in range(r)]
move = [(0,1), (0,-1), (-1,0), (1,0)]
no = []
def dfs(visit, now_y, now_x, cnt):
    for i,j in move:
        if 0 <= now_y + i < r and 0 <= now_x + j< c:
            if not data[now_y+i][now_x+j] in visit:
                visit[data[now_y+i][now_x+j]] = 1
                dfs(visit, now_y+i, now_x+j, cnt + 1)
                del visit[data[now_y+i][now_x + j]]
            else:
                no.append(cnt) 
        else:
            no.append(cnt)
    return  max(no)
new_visit = dict()
new_visit[data[0][0]] = 1
print(dfs(new_visit, 0, 0, 1))