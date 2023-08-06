import heapq
q = []
data = []
n, k, d = map(int,input().split())
for i in range(k):
    a,b,c = map(int,input().split())
    for i in range(a,b+1,c):
        heapq.heappush(q, i)

while d > 0:
    d-=1
    answer = heapq.heappop(q)
print(answer)
