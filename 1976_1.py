from collections import deque
n = int(input())
m = int(input())
q = deque()
parent = [i for i in range(n)]
data = [list(map(int, input().split()))for _ in range(n)]
move = list(map(int,input().split()))
index = [(row_index, col_index) for row_index, row in enumerate(data) for col_index, value in enumerate(row) if value == 1]

def get_Parent(a):
    if parent[a] == a:
        return a
    return get_Parent(parent[a])

def union(a,b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for i, j in index:
    union(get_Parent(i), get_Parent(j))



z = get_Parent(move[0] - 1)



for i in move:
    if get_Parent(i - 1) != z:
        print("NO")
        exit()

print("YES")


