n, m, c = map(int,input().split())
data = list(map(int,input().split()))
dp = [[[0] * (c+1) for _ in range(n+1)] for _ in range(m)] #dp[현재 가방][현재 보석][현재 가방에 남은 공간]

for i in range(m):
    for j in range(1,n):
        value = data[j-1]
        for z in range(1,c+1):
            if z < value:
                dp[i][j+1][z] = dp[i][j][z]
            else:
                dp[i][j+1][z] = max(dp[i][j][z], dp[i][j][z-value] + 1)
    
print(dp)