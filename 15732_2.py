import heapq
q = []
new_data = dict()
data_sort = dict()
n, k, d = map(int,input().split())
box = [0]
for i in range(k):
    a,b,c = map(int,input().split())
    for i in range(a,b+1,c):
        if i in data_sort:
            data_sort[i] +=1
        else:
            data_sort[i] = 1

sorting = sorted(data_sort.items())
#print(sorting)
for i in range(len(sorting)):
    box.append(sorting[i][1])

for i in range(1, len(sorting)+1):
    box[i] += box[i-1]

#print(box)
left = 1
right = len(sorting)
mid = (left + right)//2
while left <= right:
    mid = (left + right)//2
    if d > box[mid]:
        left = mid + 1
    else:
        answer = mid 
        right = mid - 1

print(sorting[answer - 1][0])   

