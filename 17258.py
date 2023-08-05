n,m,k,t = map(int,input().split())
n+=1
pp = [list(map(int,input().split())) for _ in range(m)]
time = [0] * (n+1) # 현재 시간에 파티에 초대받은 손님 수, 친구들 수
for i in range(m):
    for j in range(pp[i][0],pp[i][1]+1):
        time[j] += 1
dp = [[-1 for _ in range(k+1)] for _ in range(n+1)] #dp[i][j] == 현재 i시간이며 친구 수가 j일 때
print(time)



def solve(now, can, prev_friend, cnt):
    global dp
    if can < 0 :
        return 0
    if now == n: 
        return cnt

    if dp[now][can] != -1:
        return dp[now][can]
    
    if time[now] >= t:
        dp[now][can] = solve(now+1, can, 0, cnt + 1)
        #print(dp[now][can])
        return dp[now][can]
    elif t > (time[now] + prev_friend):
        dp[now][can] = max(solve(now+1, can - (t-(time[now] + prev_friend)), t-time[now], cnt + 1), solve(now+1, can, prev_friend, cnt))
        #prev_friend(dp[now][can])
        return dp[now][can]
    else:
        dp[now][can] = solve(now+1, can, prev_friend, cnt + 1)
        return dp[now][can]

print(solve(0,k,0,0))

print(dp)