import heapq
n,m,x = map(int,input().split())
Max = 100*100000
city = [[Max for j in range(n+1)]for i in range(n+1)]
for i in range(1,n+1):
    city[i][i] = 0
road = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    city[a][b] = c
    if road[a] == None:
        road[a] = list(b)
    else:
        road[a].append(b)
# for i in range(1, n+1):
#     for a,b in road:
#         city[i][b] = min(city[i][b], city[i][a] + city[a][b])

for i in range(1, n+1):
    hq = []
    heapq.heappush(hq, (0, i))
    while hq:
        now_cost, now = heapq.heappop(hq)
        if city[i][now] < now_cost:
            continue
        for next in road[now]:
            city[i][next] = min(city[i][next], now_cost + city[now][next])
            if city[i][next] == now_cost + city[now][next]:
                heapq.heappush(hq,(city[i][next], next))


answer = []
for i in range(1,n+1):
    answer.append(city[i][x] + city[x][i])
#print(answer)
print(max(answer))