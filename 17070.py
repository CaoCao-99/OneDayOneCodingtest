def DFS(y,x,pos, cnt):
    if y == n-1 and x == n-1:
        cnt+=1
        return cnt
    if pos == 0:
        if x+1 < n and pipe[y][x+1] == 0:
            cnt = DFS(y,x+1, 0,cnt)
        if x+1 < n and y + 1 < n and pipe[y+1][x+1] == 0 and pipe[y][x+1] == 0 and pipe[y+1][x] == 0:
            cnt = DFS(y+1,x+1, 1 , cnt)    
    if pos == 1:
        if x+1 < n and pipe[y][x+1] == 0:
            cnt = DFS(y,x+1, 0,cnt)
        if y+1 < n and pipe[y+1][x] == 0:
            cnt = DFS(y+1,x, 2,cnt)
        if x+1 < n and y + 1 < n and pipe[y+1][x+1] == 0 and pipe[y][x+1] == 0 and pipe[y+1][x] == 0:
            cnt = DFS(y+1,x+1, 1 , cnt)  

    if pos == 2:
        if y+1 < n and pipe[y+1][x] == 0:
            cnt = DFS(y+1,x, 2,cnt)
        if x+1 < n and y + 1 < n and pipe[y+1][x+1] == 0 and pipe[y][x+1] == 0 and pipe[y+1][x] == 0:
            cnt = DFS(y+1,x+1, 1 , cnt)  
    return cnt

n = int(input())
pos = ((0,1), 0) # start (y,x), (0 : 가로, 1 : 대각선, 2 : 세로)
pipe = [list(map(int,input().split())) for _ in range(n)]

print(DFS(0,1,0,0))
