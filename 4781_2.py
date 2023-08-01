from collections import deque
answer = []


while True:
    n, budget = map(float,input().split())
    n = int(n)
    budget = int(budget*100)
    candy = []
    if n == 0 and budget == 0:
        break
    for i in range(n):
        c, p = map(float,input().split())
        candy.append([int(c),int(p*100)])
    dp = [0] * (budget+1)
    for i in range(1, budget+1):
        for j in range(n):
            if i - candy[j][1] >=0:
                dp[i] = max(dp[i], dp[i-candy[j][1]] + candy[j][0])
    answer.append(dp[budget])        



for i in answer:
    print(i)