from itertools import combinations,permutations
import copy
n, s = map(int,input().split())
data = list(map(int,input().split()))
data = sorted(data)
left = []
right = []
real_left = []
real_right = dict()

for i in range(n):
    if i < n//2:
        left.append(data[i])
    else:
        right.append(data[i])
        if data[i] not in real_right:
            real_right[data[i]] = 1
        else:
            real_right[data[i]] += 1

real_left = copy.deepcopy(left)

for i in range(2,len(left)+1):
    a = combinations(left, i)
    for j in a:
        now = sum(j)
        real_left.append(now)


for i in range(2,len(right)+1):
    a = combinations(right, i)
    for j in a:
        now = sum(j)
        if now not in real_right:
            real_right[now] = 1
        else:
            real_right[now] += 1
answer = 0
answer += real_left.count(s)
if s in real_right:
    answer += real_right[s]

real_left = sorted(real_left)
real_right = sorted(real_right.items())


for i in real_left:
    l = 0
    r = len(real_right)-1
    mid = (l+r) // 2
    while l <= r:
        mid = (l+r)//2
        if mid < 0 or mid >= len(real_right):
            break
        if s < real_right[mid][0] + i:
            r = mid - 1
        if s > real_right[mid][0] + i:
            l = mid + 1
        if s == real_right[mid][0] + i:
            answer += real_right[mid][1]
            break

print(answer)       
