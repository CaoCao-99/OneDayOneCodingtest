import copy
n, m = map(int,input().split())
data = [[0 for _ in range(m+1)]] + [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
answer = [[[0 for _ in range(m+1)] for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):#돈
    for j in range(1,m+1):#회사
        dp[j][i] = max(data[i][j], dp[j-1][i])
        if dp[j][i] == data[i][j]:
            answer[i][j][j] = i
        else:
            answer[i][j] = copy.deepcopy(answer[i][j-1])
        for dev in range(1, i+1):#분할 투자
            dp[j][i] = max(data[i-dev][j] + dp[j-1][dev], dp[j][i])
            if dp[j][i] == data[i-dev][j] + dp[j-1][dev]:
                answer[i][j] = copy.deepcopy(answer[dev][j-1])
                answer[i][j][j] = i - dev


print(dp[m][n])
print(*answer[n][m][1:])
