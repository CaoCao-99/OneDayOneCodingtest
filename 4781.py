from collections import deque
answer = []
while True:
    n, budget = map(float,input().split())
    n = int(n)
    if n == 0 and budget == 0:
        break
    candy = [list(map(float,input().split()))for i in range(n)]
    visit = dict()
    q = deque()
    q.append(0)
    visit[0] = 0
    while q:
        now = q.popleft()
        for i,j in candy:
            if now + j <= budget:
                if not (now + j) in visit:
                    visit[now+j] = visit[now] + i
                    q.append(now + j)
                else:
                    if visit[now+j] < visit[now] + i:
                        visit[now+j] = visit[now] + i
                        #q.append(now+j)
    answer.append(max(visit.values()))
for i in answer:
    print(i)
    