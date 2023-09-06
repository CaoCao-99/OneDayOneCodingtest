import heapq
n = int(input())
data = list(map(int,input().split()))
maxq = []
minq = []

for i in data:
    heapq.heappush(minq, i )
    heapq.heappush(maxq, -i)

answer = - minq[0] - maxq[0]
first_max = - maxq[0]
while (minq[0]) <= first_max:
    mi = heapq.heappop(minq)
    ma = abs(heapq.heappop(maxq))
    answer = min(answer,ma-mi)
    heapq.heappush(maxq, - abs(mi*2))
    heapq.heappush(minq, mi * 2)
    heapq.heappush(maxq, -ma)

print(answer)