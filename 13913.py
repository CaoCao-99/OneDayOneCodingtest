import sys
sys.setrecursionlimit(10**7)
n, k = map(int,input().split())
time = [[100000000, 10000000] for _ in range(100001)]
move = [-1,1]
q = [n]
time[n] = [0, 0]
path = []
def pp(k):
    if k == n:
        print(n, end = ' ')
        return
    pp(time[k][1])
    print(k, end = ' ')

while q:
    now = q.pop(0)
    if now == k:
        idx = now
        while idx != n:
            path.append(idx)
            idx = time[idx][1]
        path.append(n)
    for i in move:
        if 0 <= now + i <= 100000 and time[now + i][0] > time[now][0] + 1:
            time[now + i][0] = time[now][0] + 1 
            time[now + i][1] = now
            q.append(now+i)

    if 0 <= (now * 2) <= 100000 and time[now * 2][0] > time[now][0] + 1:
        time[now * 2][0] = time[now][0] 
        time[now * 2][1] = now
                            
        q.append(now*2)

print(time[k][0])
print(*path[::-1])

#print(sys.getsizeof(time), sys.getsizeof(path))
#pp(k)

#
#5 17