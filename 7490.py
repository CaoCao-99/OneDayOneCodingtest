from collections import deque
n = int(input())
sign = [' ','+', '-']
real_answer = []
for i in range(n):
    k = int(input())
    data = range(1,k+1)
    d = dict()
    q = deque()
    for j in sign:
        q.append(j)
        d[j] = j
    while q:
        now = q.popleft()
        if len(now) == k - 1:
            answer = '1'
            for a in range(k-1):
                answer += now[a]
                answer += str(data[a+1])
            co = answer
            co = co.replace(" ","")
            if eval(co) == 0:
                #print(answer)
                real_answer.append(answer)
            continue
        for j in sign:
            next = now + j
            if not next in d:
                q.append(next)
                d[next] = 1
    #print()       
    real_answer.append('')  
for i in real_answer:
    print(i)

