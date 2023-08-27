from collections import deque
n, m, c = map(int,input().split())
data = list(map(int,input().split()))
q = deque()

for i in range(m):
    for j in range(1,n):
        value = data[j-1]
        for z in range(1,c+1):
            if z < value:
                dp[i][j+1][z] = dp[i][j][z]
            else:
                dp[i][j+1][z] = max(dp[i][j][z], dp[i][j][z-value] + 1)
    
print(dp)