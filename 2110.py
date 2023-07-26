n, k = map(int,input().split())
data = [int(input()) for i in range(n)]
data = sorted(data)
dist = []
for i in range(len(data) - 1):
    dist.append(data[i+1] - data[i])
    
print(dist)
low = min(dist)
high = sum(dist)
mid = (low + high)//2

while low <= high:
    mid = (low+high)//2
    cnt = 0
    cntcnt = 0
    answer_a = high
    low_check = False
    for i in range(len(dist)):
        cnt += dist[i]
        if cnt > mid:
            cnt = dist[i]
            cntcnt+=1
            answer_a = min(answer_a, cnt - dist[i])
        if cntcnt >= k-1:
            low_check = True
            break
    if low_check:
        answer = answer_a
        low = mid + 1
    else:
        high = mid - 1

print(high)