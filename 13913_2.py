import sys

n, k = map(int,input().split())
time = [100000000 for _ in range(100001)]
move = [-1,1]
moving = ['' for _ in range(100001)]
q = [n]
moving[n] = str(n)
time[n] = 0
while q:
    now = q.pop(0)
    for i in move:
        if 0 <= now + i <= 100000 and time[now + i] > time[now] + 1:
            next = moving[now] + ' ' + str(now + i)
            moving[now + i] = next
            time[now + i] = time[now] + 1
            q.append(now+i)

    if 0 <= (now * 2) <= 100000 and time[now * 2] > time[now] + 1:
        time[now * 2] = time[now] + 1
        next = moving[now] + ' ' + str(2 * now)
        moving[now * 2 ] = next
        q.append(now*2)

print(time[k])
print(moving[k])
#5 17