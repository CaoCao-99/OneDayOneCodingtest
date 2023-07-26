n, k = map(int,input().split())
data = [int(input()) for i in range(n)]
data = sorted(data)
dist = []
for i in range(len(data) - 1):
    dist.append(data[i+1] - data[i])
low = min(dist)
high = sum(dist)
mid = (low + high)//2

while low <= high:
    mid = (low+high)//2
    cnt = 0
    cntcnt = 0
    low_check = False
    for i in range(len(dist)):
        cnt += dist[i]
        if cnt >= mid:
            cnt = 0
            cntcnt+=1
        if cntcnt >= k-1:
            low_check = True
            break
    if low_check:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)