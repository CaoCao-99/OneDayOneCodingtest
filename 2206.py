import sys
from collections import deque
input = sys.stdin.readline
n , m = map(int,input().split())
tile = [input() for _ in range(n)]
dp = [[[1000000000 for _ in range(2)]for _ in range(m)]for _ in range(n)]
move = [(-1,0),(1,0),(0,1),(0,-1)]
q = deque()
q.append([0,0,1])
dp[0][0][1] = 1
while q:
    y,x,crush = q.popleft()
    for i,j in move:
        if 0 <= y+i <n and 0 <= x+j < m:
            if tile[y+i][x+j] == '1' and dp[y+i][x+j][0] > dp[y][x][1] + 1:#벽인 경우
                if crush == 1:
                    dp[y+i][x+j][0] = dp[y][x][1] + 1
                    q.append([y+i,x+j,0])
            elif tile[y+i][x+j] == '0' and dp[y+i][x+j][crush] > dp[y][x][crush] + 1:
                    dp[y+i][x+j][crush] = dp[y][x][crush] + 1
                    q.append([y+i,x+j,crush])

if min(dp[n-1][m-1]) == 1000000000:
    print(-1)
else:
    print(min(dp[n-1][m-1]))