n,m = map(int,input().split())
data = [input() for _ in range(n)]
move = [(1,0), (-1,0), (0,-1), (0,1)]
answer = 0

def DFS(y,x,visit):
    
    for i,j in move:
        if 0<=y+i<n and 0<=x+j<m and visit[y+i][x+j] > visit[y][x] + 1 and data[y+i][x+j] == 'L':
            visit[y+i][x+j] = visit[y][x] + 1
            DFS(y+i,x+j,visit)
    return visit


for i in range(n):
    for j in range(m):
        if data[i][j] == 'L':
            new_visit = [[999999999 for _ in range(m)] for _ in range(n)]
            new_visit[i][j] = 0
            a = DFS(i,j,new_visit)
            for i in range(n):
                for j in range(m):
                    if a[i][j] != 999999999:
                        answer = max(answer, a[i][j])
print(answer)
            