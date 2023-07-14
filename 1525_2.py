move = [(-1,0), (1,0), (0,1), (0,-1)]
data = ""
for i in range(3):
    a = list(map(int,input().split()))
    data += str(a[0]) + str(a[1]) + str(a[2])

visit = dict()
q = []
q.append((data, 0))

while q:
    now, count = q.pop(0)
    if now == "123456780":
        print(count)
        exit()
    n = now.index('0')
    n_y = n//3
    n_x = n%3
    for i,j in move:
        if 0 <= n_y + i < 3 and  0 <= n_x + j < 3:
            change = [0 for _ in range(9)]
            for aa in range(9):
                change[aa] = int(now[aa])
            change[n_y * 3 + n_x], change[(n_y + i) * 3 + n_x + j] = change[(n_y + i) * 3 + n_x + j], change[n_y * 3 + n_x]
            new_c = ""
            for i in range(9):
                new_c += str(change[i])
            if not new_c in visit:
                visit[new_c] = count
                q.append((new_c, count + 1))
print(-1)