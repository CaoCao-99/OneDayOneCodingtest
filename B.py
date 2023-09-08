import sys
input = sys.stdin.readline
n, m = map(int, input().split())
sec = list(map(int,input().split()))
thi = list(map(int,input().split()))
sec = sorted(sec)
thi = sorted(thi)
b_sec = -100
b_thi = -360
s_cnt = 0
t_cnt = 0
for i in range(n):
    if sec[i] >= b_sec + 100:
        b_sec = sec[i]
        s_cnt +=1
for i in range(m):
    if thi[i] >= b_thi + 360:
        b_thi = thi[i]
        t_cnt += 1

print(s_cnt, t_cnt)