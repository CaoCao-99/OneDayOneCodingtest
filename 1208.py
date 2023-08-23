from itertools import combinations,permutations
import copy
n, s = map(int,input().split())
data = list(map(int,input().split()))
data = sorted(data)
left = []
right = []
for i in range(n):
    if i < n//2:
        left.append(data[i])
    else:
        right.append(data[i])

real_left = copy.deepcopy(left)

real_right = copy.deepcopy(right)

for i in range(2,len(left)+1):
    a = combinations(left, i)
    for j in a:
        real_left.append(sum(j))

for i in range(2,len(right)+1):
    a = combinations(right, i)
    for j in a:
        real_right.append(sum(j))

answer = 0
real_left = sorted(real_left)
real_right = sorted(real_right)
answer += real_left.count(s)
answer += real_right.count(s)
for i in real_left:
    l = 0
    r = len(real_right)-1
    mid = (l+r) // 2
    while l <= r:
        mid = (l+r)//2
        if mid < 0 or mid >= len(real_right):
            break
        if s < real_right[mid] + i:
            r = mid - 1
        if s > real_right[mid] + i:
            l = mid + 1
        if s == real_right[mid] + i:
            answer += real_right.count(real_right[mid])
            break

print(answer)       
