n, k = map(int,input().split())
coin = [int(input())for _ in range(n)]
dp = [9999999] * (k+1)
dp[0] = 0

for i in range(1,k+1):
    for j in coin:
        if i >= j and dp[i] > dp[i-j] + 1:
            dp[i] = dp[i-j] + 1

if dp[k] == 9999999:
    print(-1)
print(dp[k])