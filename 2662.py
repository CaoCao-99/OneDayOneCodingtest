import copy
n, m = map(int,input().split())
data = [[0 for _ in range(m+1)]] + [list(map(int,input().split())) for _ in range(n)]
print(data)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
print(dp)
answer = [0] * (n+1)


for i in range(1, n+1): #현재 돈
    new_arr = copy.deepcopy(dp)
    new_plus = 0
    new_new_plus = 0
    for j in range(1, m+1): #회사
        if dp[i-1][j] != 0:
            new_plus = data[dp[i-1][j] + 1][j] - data[dp[i-1][j]][j]
            if new_plus + answer[i-1]> answer[i]:
                answer[i] = new_plus + answer[i-1]
                new_arr[i][j] = dp[i-1][j] + 1
        else:
            new_new_plus = data[i][j]
        if new_plus + answer[i-1] > new_new_plus:
            
    dp = copy.deepcopy(new_arr)





print(answer[n])
for i in range(1,m+1):
    print(dp[n][i],end= ' ')
