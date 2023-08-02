import heapq
n = int(input())
data = [1000 for _ in range(n)]
if n == 1:
    print(0)
    exit()
first_queue = []
second_queue = []
answer = 0
for i in data:
    heapq.heappush(first_queue,i)
first = heapq.heappop(first_queue)
heapq.heappush(second_queue,first)
# 2233 -> (2+2) + (3+3)
while first_queue:
    now = heapq.heappop(first_queue)
    best = heapq.heappop(second_queue)
    if now < best:
        heapq.heappush(second_queue,now)
        heapq.heappush(second_queue,best)
    else:
        heapq.heappush(second_queue, now+best)
        answer += now+best

# print(second_queue)
# print(sum(second_queue))



if len(second_queue) == 1:
    print(answer)
else:
    print(answer + sum(second_queue))
