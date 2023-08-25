from collections import deque
n = int(input())
m = int(input())
q = deque()
data = [list(map(int, input().split()))for _ in range(n)]
index = [(row_index, col_index) for row_index, row in enumerate(data) for col_index, value in enumerate(row) if value == 1]

for i, j in index:
    q.append([i])
    q.append([j])

while  q:
    now = q.popleft()
    

for i in range(n):
    for j in range(n):
        if data[i][j] == 