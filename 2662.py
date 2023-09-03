import copy
n, m = map(int,input().split())
data = [[0 for _ in range(m+1)]] + [list(map(int,input().split())) for _ in range(n)]
print(data)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
answer = [0] * (n+1)

for a in range(1,n+1):#현재 회사 번호
    for b in range(1,a+1):
        for c in range(1, m+1):# 현재 회사에 쓸 금액
            dp[a][c] = max(dp[])



#

#dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])