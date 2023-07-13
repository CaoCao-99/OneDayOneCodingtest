dp = [[[999999999 for i in range(5)] for _ in range(5)] for _ in range(100000)]
data = list(map(int,input().split()))
dp[0][0][data[0]] = 2
dp[0][data[0]][0] = 2


n = len(data) - 1


def adding(a, b):
    if a == b:
        return 1
    elif a == 0 :
        return 2
    elif abs(b-a)%2 == 0:
        return 4
    else:
        return 3



for i in range(1, n):

    #오른발 고정 왼발 움직임
    for r in range(5):
        for l in range(5):
            if r != l and r != data[i]:
                dp[i][data[i]][r] = min(dp[i][data[i]][r], dp[i-1][l][r] + adding(l, data[i]))

    #왼발 고정 오른발 움직임
    for l in range(5):
        for r in range(5):
            if l != r and l != data[i]:
                dp[i][l][data[i]] = min(dp[i][l][data[i]], dp[i-1][l][r] + adding(r, data[i]))


print(min(min(dp[n-1])))

print(dp[-1])