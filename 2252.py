from collections import deque
n, m = map(int,input().split())
visit =  [False] * 32001
check = [False] * 32001
count = [0] * 32001
out = [[] for _ in range(32001)]
for i in range(m):
    a,b = map(int,input().split())
    visit[a] = True
    visit[b] = True
    out[a].append(b)
    count[b] += 1

for i in range(1,n+1):
    if visit[i]:
        if count[i] == 0:
            count[i] += 1
            out[0].append(i)

q = deque()
q.append(0)
check[0] = True
answer = []

while q:
    now = q.popleft()
    answer.append(now)
    for i in out[now]:
        count[i] -= 1
        if count[i] == 0:
            q.append(i)
    # for i in range(1,n+1):
    #     if visit[i] and count[i] == 0 and check[i] == False:
    #         check[i] = True
    #         q.append(i)

for i in range(1,n+1):
    if visit[i] == False:
        answer.append(i)
for i in range(1,n+1):
    print(answer[i], end = ' ')