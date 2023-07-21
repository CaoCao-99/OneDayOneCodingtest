import sys
n, k = map(int,input().split())
visit = [-1 for _ in range(100001)]
move = [-1,1]
q = [(n,0)]
visit[n] = n
path = []
def pp(k):
    if k == n:
        print(n, end = ' ')
        return
    pp(time[k][1])
    print(k, end = ' ')

while q:
    now, time = q.pop(0)
    if now == k:
        print(time)
        idx = now
        while idx != n:
            path.append(idx)
            idx = visit[idx]
        path.append(n)
        break
    for i in move:
        if 0 <= now + i <= 100000 and visit[now + i] == -1:
            visit[now + i] = now
            q.append((now+i, time + 1))

    if 0 <= (now * 2) <= 100000 and visit[now * 2] == -1:
        visit[now * 2] = now
        q.append((now*2, time + 1))


print(*path[::-1])

#print(sys.getsizeof(time), sys.getsizeof(path))
#pp(k)

#
#5 17