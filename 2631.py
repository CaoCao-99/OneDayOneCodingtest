n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

dp = [1 for j in range(n)]

for i in range(1,n):
    for j in range(i):
        if data[j] < data[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j]+1

print(n - max(dp))



# dp[0], dp[1] = data[0] < data[1] , dp[1] < dp[0]+1, dp[2] = (0.2), (1,2), dp[3] = (0,3),(1,3),(2,3)