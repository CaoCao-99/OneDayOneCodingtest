from itertools import combinations
import gc
import copy
n = int(input())
if n == 1:
    print(0)
    exit()
data = list(map(int,input().split()))

answer = 0
for i in range(n):
    new_data = copy.deepcopy(data)
    new_data.remove(data[i])
    answer_arr = list((combinations(new_data, 2)))
    arr = set()
    for a,b in answer_arr:
        if a+b not in arr:
            arr.add(a+b)
    arr = sorted(arr)
    left = 0
    right = len(arr)
    mid = (left+right)//2
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == data[i]:
            answer += 1
            break
        if arr[mid] > data[i]:
            right = mid - 1
        else:
            left = mid + 1


    

    
print(answer)