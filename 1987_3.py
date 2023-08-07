import sys
input = sys.stdin.readline
r, c = map(int,input().split())
data = [input() for _ in range(r)]
move = [(0,1), (0,-1), (-1,0), (1,0)]
def dfs(now_y, now_x, cnt):
    global answer
    answer = max(answer , cnt)
    for i,j in move:
        if 0 <= now_y + i < r and 0 <= now_x + j< c:
            if not data[now_y+i][now_x+j] in visit:
                visit.add(data[now_y+i][now_x+j])
                dfs(now_y+i, now_x+j, cnt + 1)
                visit.remove(data[now_y+i][now_x + j])
visit = set()
visit.add(data[0][0])
answer = 0
dfs(0, 0, 1)
print(answer)