import copy
import sys
sys.setrecursionlimit(10**6)
n = int(input())
start = input()
start = [int(i) for i in start]
want = input()
want = [int(i) for i in want]
print(want)
answer = 1000000000000000
dp = [[-1] * 10 for _ in range(10001)]
choice = [[0] * 10 for _ in range(10001)]
def change(now, cost):
    if dp[now][cost] != -1:
        return dp[now][cost]
    s = (start[now] + cost) % 10
    e = want[now]
    if now == n - 1:
        choice[now][cost] = e - s
        dp[now][cost] = abs(e-s)
        return dp[now][cost]
    now_cost = 0
    left = 0
    if s > e:
        now_cost = s- e
    else:
        now_cost = (e - s + 10)%10
    left = change(now + 1, cost) + now_cost

    if e > s:
        now_cost2 = e-s
    else:
        (10 - e + s)%10
    right = change(now + 1, (cost+now_cost2)%10) + now_cost2
    if left < right:
        choice[now][cost] = -now_cost
    else:
        choice[now][cost] = now_cost2
    dp[now][cost] = min(left, right)
    return dp[now][cost]

def rec(now, cost):
    if now == n:
        return
    if choice[now][cost] != 0:
        print(now + 1, choice[now][cost])
    if choice[now][cost] > 0:
        rec(now + 1, (cost + choice[now][cost]) % 10)
    else:
        rec(now + 1, cost)

print(change(0,0))
rec(0,0)
