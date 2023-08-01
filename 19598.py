import heapq

n = int(input())
if n == 1:
    print(1)
    exit()
data = [list(map(int,input().split()))for _ in range(n)]
first_q = []
second_q = []

for i,j in data:
    heapq.heappush(first_q,[i,j])
s,e = heapq.heappop(first_q)
heapq.heappush(second_q, [e,s])
cnt = 1
while first_q:
    now_start, now_end = heapq.heappop(first_q)
    best_end, best_start = heapq.heappop(second_q)
    if best_end > now_start:
        heapq.heappush(second_q, [now_end, now_start])
        heapq.heappush(second_q, [best_end,best_start]) #다시 넣어주기!!
        cnt+=1
    else:
        heapq.heappush(second_q, [now_end, now_start])

print(cnt)