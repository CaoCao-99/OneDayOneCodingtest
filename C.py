import sys
import math
input = sys.stdin.readline
n, m, k = map(int, input().split())
c_d = []
boss = []
answer = []

for i in range(n):
    c_d.append(int(input()))
for i in range(k):
    boss.append(list(map(int,input().split())))
for i in range(n):
    dp = [[0 for _ in range(60*15+1)]for _ in range(len(boss))]
    for a in range(len(boss)-1):
        for b in range(60*15+1):
            value, need_d = boss[a][1], math.ceil(boss[a][0]//c_d[i])
            if b < need_d:
                dp[a+1][b] = dp[a][b]
            else:
                dp[a+1][b] = max(dp[a][b - need_d] + value, dp[a][b])
    answer.append(dp[-1][-1])

answer = sorted(answer, reverse=True)
ans = 0
for i in range(m):
    ans += answer[i]
print(ans)