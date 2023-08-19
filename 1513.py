import sys
input = sys.stdin.readline
n,m,c = map(int, input().split())
dp = [[[[-1] * (c+1) for _ in range(c+1)] for _ in range(m+1)] for _ in range(n+1)]
orak = [[0] * 51 for i in range(51)]

def visit(a,b,c,d):
    if a < 1 or b < 1 or c < 0:
        return 0
    if dp[a][b][c][d] != -1:
        return dp[a][b][c][d]
    dp[a][b][c][d] = 0
    if orak[a][b] == 0:
        dp[a][b][c][d] = visit(a-1,b,c,d) + visit(a,b-1,c,d)
    elif orak[a][b] == d:
        for i in range(d):
            dp[a][b][c][d] += visit(a-1,b,c-1,i) + visit(a,b-1,c-1,i)
    return dp[a][b][c][d]
     
#오락실 개수1,를  때, 모든 오락실 번호를 넣고 출발




for i in range(c):
    q,w = map(int,input().split())
    orak[q][w] = i+1

if orak[1][1] != 0:
    dp[1][1][1][orak[1][1]] = 1
else:
    dp[1][1][0][0] = 1

 
for i in range(c+1):
    answer = 0
    for j in range(c+1):
        answer += visit(n,m,i,j)
    print((answer%1000007), end = ' ')