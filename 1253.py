from itertools import combinations
n = int(input())
if n == 1:
    print(0)
    exit()
data = list(map(int,input().split()))
d = dict()
for i in data:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
d = sorted(d.items())
answer_arr = list((combinations(data, 2)))
arr = set()
for i,j in answer_arr:
    if i+j not in arr :
        arr.add(i+j)
arr = sorted(arr)
answer = 0


for i,j in d:
    left = 0
    right = len(arr)
    mid = (left+right)//2
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == i:
            answer += j
            break
        if arr[mid] > i:
            right = mid - 1
        else:
            left = mid + 1

    
print(answer)