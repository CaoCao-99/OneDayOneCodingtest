import sys
from collections import deque
input = sys.stdin.readline
tile = []
n , m = map(int,input().split())
for _ in range(n):
    row = list(str(input().rstrip()))
    tile.append(list(map(int, row)))
dp = [[[0 for _ in range(2)]for _ in range(m)]for _ in range(n)]
move = [(-1,0),(1,0),(0,1),(0,-1)]
q = deque()
q.append([0,0,1])
dp[0][0][1] = 1
while q:
    y,x,crush = q.popleft()
    if y == n-1 and x == m-1:
        print(dp[y][x][crush])
        exit()
    for i,j in move:
        if 0 <= y+i <n and 0 <= x+j < m:
            if tile[y+i][x+j] == 1:#벽인 경우
                if crush == 1:
                    dp[y+i][x+j][0] = dp[y][x][1] + 1
                    q.append([y+i,x+j,0])
            elif tile[y+i][x+j] == 0 and dp[y+i][x+j][crush] == 0:
                    dp[y+i][x+j][crush] = dp[y][x][crush] + 1
                    q.append([y+i,x+j,crush])

if min(dp[n-1][m-1]) == 0:
    print(-1)