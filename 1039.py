from collections import deque
import copy
n, k = map(int,input().split())
n = str(n)
data = []
for i in range(len(n)):
    data.append(int(n[i]))

answer = [[] for _ in range(k+1)]
answer[0].append(data)
q = deque()
q.append([data,0])

while q:
    now, now_cnt = q.popleft()
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            copy_now = copy.deepcopy(now)
            if (not(i == 0 and now[j] == 0)) and now_cnt + 1 <=k:
                copy_now[i],copy_now[j] = copy_now[j],copy_now[i]
                in_data = ''
                for z in copy_now:
                    in_data += str(z)
                if not in_data in answer[now_cnt+1]:
                    answer[now_cnt+1].append(in_data)
                    q.append([copy_now, now_cnt+1])

ans = -1
if answer[k]:
    for i in answer[k]:
        ans = max(ans,int(str(i)))
    print(ans)
else:
    print(-1)



# 1234 1

