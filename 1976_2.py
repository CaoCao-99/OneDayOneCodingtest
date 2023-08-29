from collections import deque
n = int(input())
m = int(input())
root = [[] for _ in range(n)]
data = [list(map(int, input().split()))for _ in range(n)]
move = list(map(int,input().split()))
index = [(row_index, col_index) for row_index, row in enumerate(data) for col_index, value in enumerate(row) if value == 1]
visit = [[0] * n for _ in range(n)]

def check(aa):
    for i in range(1,m):
        past = move[i-1] - 1
        if aa[past][move[i] - 1] == 0:
            print("NO")
            exit()
    print("YES")


for i, j in index:
    root[i].append(j)
    root[j].append(i)


for i in range(n):
    visit[i][i] = 1

for i in range(n):
    q = deque()
    q.append(i)
    while  q:
        now = q.popleft()
        for next in root[now]:
            if visit[i][next] == 0:
                visit[i][next] = 1
                q.append(next)

check(visit)
