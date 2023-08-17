import heapq
n = int(input())
for i in range(n):
    k = int(input())
    data = list(map(int,input().split()))
    q = []
    answer = 0
    for j in data:
        heapq.heappush(q,j)
    first = heapq.heappop(q)
    while q:
        second = heapq.heappop(q)
        heapq.heappush(q,first + second)
        answer += first+second
        first = heapq.heappop(q)
    print(answer)