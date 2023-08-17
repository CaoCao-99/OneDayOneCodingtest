import heapq
n,m = map(int,input().split())
go = [[] for _ in range(n+1)]
dp = [10000000000] * (n+1)

for i in range(m):
    a,b,c = map(int,input().split())
    go[a].append([b,c])
    go[b].append([a,c])


q = []
heapq.heappush(q, [0, 1])
while q:
    now_cost , now = heapq.heappop(q)
    for a,b in go[now]:
        if dp[a] > now_cost + b:
            dp[a] = now_cost + b
            heapq.heappush(q, [now_cost + b, a])
print(dp[n])