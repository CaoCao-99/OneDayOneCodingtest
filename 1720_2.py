n = int(input())

dp = [0 for i in range(31)]

dp[1] = 1
dp[2] = 3
if n == 1 or n == 2:
    print(dp[n])
    exit()
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2
answer = 0

#팰린드롬인 경우
if n%2 == 0:
    answer += dp[n//2] + 2 * dp[n//2 - 1]
else:
    answer += dp[n//2]

answer += (dp[n] - answer)//2

print(answer)
