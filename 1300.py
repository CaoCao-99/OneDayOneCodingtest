n = int(input()) 
k = int(input())
start, end = 1, k
answer = 1
while start <= end:
    mid = (start+ end)//2
    count = 0
    for i in range(1,n+1):
        count += min(n, mid//i)
    
    if count >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
        #answer = mid
print(answer)