import heapq
n = int(input())
for i in range(n):
    k = int(input())
    data = list(map(int,input().split()))
    q = []
    q2 = []
    answer = 0
    for j in data:
        heapq.heappush(q,j)
    first = heapq.heappop(q)
    heapq.heappush(q2,first)
    while q:
        second = heapq.heappop(q)
        first = heapq.heappop(q2)
        if first < second:
            heapq.heappush(q2,first + second)
            answer += first+second
        else:
            heapq.heappush(q2, second)
            heapq.heappush(q2, first)
            
    a = heapq.heappop(q2)
    while q2:
        b = heapq.heappop(q2)
        answer += a+b
        heapq.heappush(q2,a+b)
        a = heapq.heappop(q2)
        
    print(answer)