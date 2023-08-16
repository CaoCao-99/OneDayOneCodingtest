from collections import deque
n,m = map(int,input().split())
data = [input() for _ in range(n)]
move = [(1,0), (-1,0), (0,-1), (0,1)]
answer = 0

for i in range(n):
    for j in range(m):
        if data[i][j] == 'L':
            q = deque()
            q.append([i,j,0])
            visit = [[False] * m for _ in range(n)]
            visit[i][j] =True
            while q:
                y,x,cnt = q.popleft()
                for a,b in move:
                    if 0<=y+a<n and 0<=x+b<m and visit[y+a][x+b] == False and data[y+a][x+b] == 'L':
                        visit[y+a][x+b] = True
                        answer = max(answer, cnt + 1)
                        q.append([y+a,x+b,cnt+1])

print(answer)

