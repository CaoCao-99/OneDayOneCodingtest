from collections import deque
n = int(input())
m = int(input())
root = [] * (n)
data = [list(map(int, input().split()))for _ in range(n)]
index = [(row_index, col_index) for row_index, row in enumerate(data) for col_index, value in enumerate(row) if value == 1]

for i, j in index:
    root[i].append(j)
    root[j].append(i)



for i in range(n):
    q = deque()
    q.append(i)
    while  q:
        now = q.popleft()
        for next in root[now]:
            
    
