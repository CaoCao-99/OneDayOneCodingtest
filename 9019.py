from collections import deque
n = int(input())
true_answer = []
for i in range(n):
    visit = [[-1,-1,'z'] for i in range(10000)]
    original, change = map(int, input().split())
    q = deque()
    q.append(original)#현재 값, 이전에 진행한 방법
    visit[original] = [0,0,'o']
    while q:
        now = q.popleft()
        if now == change:
            answer = []
            # next = visit[change][1]
            # next_i = visit[change][2]
            while now != original:
                next = visit[now][1]
                next_i = visit[now][2]
                answer.append(next_i)
                now = next
            true_answer.append(answer[::-1])
            break
        #D
        if visit[(now*2)%10000][0] == -1:
            visit[(now*2)%10000][:] = [visit[now][0] + 1,now,'D']
            q.append((now*2)%10000)
        if visit[(now + 9999)%10000][0] == -1:
            visit[(now + 9999)%10000][:] = [visit[now][0] + 1,now,'S']
            q.append((now + 9999)%10000)
        f,e = now//1000, now % 10
        if visit[(now * 10)%10000 + f][0] == -1:
            visit[(now * 10)%10000 + f][:] = [visit[now][0] + 1,now,'L']
            q.append((now * 10)%10000 + f)
        if visit[now//10 + e * 1000][0] == -1:
            visit[now//10 + e * 1000][:] = [visit[now][0] + 1, now, 'R']
            q.append(now//10 + e * 1000)

        

for i in true_answer:
    for j in i:
        print(j,end= '')
    print()