n,m,k,t = map(int,input().split())
n+=1
pp = [list(map(int,input().split())) for _ in range(m)]
time = [0] * (n+1) # 현재 시간에 파티에 초대받은 손님 수, 친구들 수
for i in range(m):
    for j in range(pp[i][0],pp[i][1]):
        time[j] += 1
dp = [[-1 for _ in range(k+1)]  for _ in range(n+1)] #dp[i][j] == 현재 i시간이며 친구 수가 j일 때
time_block = []

first = time[1]
count = 0
for i in range(1, n+1):
    if first == time[i]:
        count +=1
    else:
        time_block.append([count, first])#시간, 인원수
        count = 1
        first = time[i]

def solve(now, can, prev_friend):
    global dp
    if now == len(time_block):
        return 0
    if dp[now][can] != -1:
        return dp[now][can]
    if time_block[now][1] >= t:
        dp[now][can] = solve(now+1, can, 0) + time_block[now][0]
    elif t > (time_block[now][1] + prev_friend) and can + prev_friend + time_block[now][1] >= t:
        dp[now][can] = max(solve(now+1, can - (t-(time_block[now][1] + prev_friend)), t - time_block[now][1]) + time_block[now][0], solve(now+1, can, prev_friend))
    elif t <= (time_block[now][1] + prev_friend):
        dp[now][can] = solve(now+1, can, prev_friend) + time_block[now][0]
    else:
        dp[now][can] = solve(now + 1, can, prev_friend)
    return dp[now][can]

print(solve(0,k,0))
