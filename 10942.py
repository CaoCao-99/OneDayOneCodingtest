import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
m = int(input())
dp = [[-1 for j in range(n)]for i in range(n)]
for i in range(n-1):#(0,1) ~ (n-2,n-1)
    if data[i] == data[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0
for i in range(n-2):
    if data[i] == data[i+2]:
        dp[i][i+2] = 1
    else:
        dp[i][i+2] = 0

for i in range(n-3,-1,-1):
    diff = n-i
    for j in range(0,i):
        if dp[j+1][j+diff-1] == 1 and data[j] == data[j+diff]:
            dp[j][j+diff] = 1
        else:
            dp[j][j+diff] = 0



slicing_data = []
for i in range(m):
    a,b = map(int,input().split())
    slicing_data.append((a-1,b-1))

for a,b in slicing_data:
    if a == b:
        print(1)
    else:
        print(dp[a][b])
        