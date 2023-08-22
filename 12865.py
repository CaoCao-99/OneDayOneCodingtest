n, k = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
dp = [0] * (n+1) #현재 물건 까지의 최대 값

def solve(now, now_w, now_c):
    if now >= n or now_w > k:
        return 0
    # if dp[now] != 0 :
    #     return dp[now]
    dp[now+1] = max(dp[now+1], max(solve(now + 1, now_w + data[now][0], now_c + data[now][1]), solve(now + 1, now_w, now_c)))
    return now_c
solve(0,0,0)
print(max(dp))
