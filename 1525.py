data = []
q = []
visited = []
point = (0,0)
move = [(1,0), (-1,0), (0,-1), (0,1)]
for i in range(3):
    data.append(list(map(int,input().split())))
for i in range(3):
    for j in range(3):
        if data[i][j] == 0:
            point = (i,j)
            q.append((0,point, data))

while q:
    count, point, visit = q.pop(0)
    print(q)
    if visit == [[1,2,3],[4,5,6],[7,8,0]]:
        print(count)
        exit()
    if visit in visited:
        continue
    visited.append(visit)
    y, x = point[0], point[1]
    for i,j in move:
        n_y,n_x = y+i, x+j
        if 0 <= n_x <3 and 0 <= n_y <3:
            new_visit = copy.deepcopy(visit)
            new_visit[y][x], new_visit[n_y][n_x] = new_visit[n_y][n_x], new_visit[y][x] 
            if not new_visit in visited:
                q.append((count+1, (n_y,n_x), new_visit))

print(-1)


