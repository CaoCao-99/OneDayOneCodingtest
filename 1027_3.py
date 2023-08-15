n = int(input())
data = list(map(int,input().split()))
answer = 0
for i in range(n):
    left = 9999999999999
    right = -9999999999999
    cnt = 0
    for j in range(i-1,-1,-1):
        incline = (data[i] - data[j]) / (i-j)
        if incline < left:
            left = incline
            cnt += 1
        
    for j in range(i+1, n):
        incline = (data[i] - data[j]) / (i-j) 
        if incline > right:
            right = incline
            cnt += 1
    answer = max(answer, cnt)
print(answer)