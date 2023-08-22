n, k = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]


for i in range(n):
    for j in range(1,k+1):
        weight = data[i][0]
        value = data[i][1]
        if j < weight:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j - weight] + value)

print(dp[n][k])