import heapq
n = int(input())
q1 = []
q2 = []
#data = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    s,e = map(int,input().split())
    heapq.heappush(q1, [s,e])

s,e = heapq.heappop(q1)
heapq.heappush(q2,e)

while q1:
    now_s, now_e = heapq.heappop(q1)
    al_e = heapq.heappop(q2)
    if now_s >= al_e:
        heapq.heappush(q2, now_e)
    else:
        heapq.heappush(q2,al_e)
        heapq.heappush(q2,now_e)

print(len(q2))