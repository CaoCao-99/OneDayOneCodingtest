n,m,k = map(int,input().split())
dp = [[[-1] * (221) for _ in range(220+1)] for _ in range(10+1)]

def solve(length, summ, last):
    if length > n or summ > m:
        return 0
    if dp[length][summ][last] != -1:
        return dp[length][summ][last]    
    result = 0
    for i in range(last, m+1):
        result += solve(length+1,summ + i,i)
    dp[length][summ][last] = result
    return dp[length][summ][last]

def get_answer(length, summ, last, k):
    if length == n:
        return
    for i in range(last, m+1):
        if dp[length + 1][summ + i][i] == -1:
            continue
        if k > dp[length + 1][summ + i][i]:
            k -= dp[length + 1][summ + i][i]
            continue
        print(i, end = ' ')
        get_answer(length + 1 , summ + i, i, k)
for i in range(1, m+1):
    dp[n][m][i] = 1
solve(0,0,1)
get_answer(0,0,1,k)
