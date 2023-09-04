import copy
n, m = map(int,input().split())
data = [[0 for _ in range(m+1)]] + [list(map(int,input().split())) for _ in range(n)]
print(data)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
answer = [0] * (n+1)

for i in range(1,n+1):
    for j in range(1,m+1):
        for dev in range(i+1):
            dp[j][i] = max(data[i][j])



#

#dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])