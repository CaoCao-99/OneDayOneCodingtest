import heapq
n = int(input())
data = [int(input()) for _ in range(n)]
if n == 1:
    print(0)
    exit()
first_queue = []
answer = 0
for i in data:
    heapq.heappush(first_queue,i)
now = heapq.heappop(first_queue)

# 2233 -> (2+2) + (3+3)

while first_queue:
    next = heapq.heappop(first_queue)
    if next < now:
        heapq.heappush(first_queue,now)
        heapq.heappush(first_queue,next)
    else:
        heapq.heappush(first_queue, now+next)
        answer += now+next
    now = heapq.heappop(first_queue)

print(answer)
print(first_queue)



