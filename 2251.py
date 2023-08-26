from collections import deque
a,b,c = map(int,input().split())
q = deque()
d = dict()
q.append([0,0,c])
d[str(0)+ 'a' + str(0) + 'b' + str(c) + 'c'] = 1
answer = set()

def find(q,w,e):
    send = []
    if q < a:
        send.append(0)
    if w < b:
        send.append(1)
    if e < c:
        send.append(2)
    return send


while q:
    n_a,n_b,n_c = q.popleft()
    if n_a == 0 and n_c > 0:
        answer.add(n_c)
    can_put = find(n_a,n_b,n_c)
    for i in can_put:
        if i == 0:
            if n_b > 0:
                if n_b > a - n_a and str(a) +'a'+str(n_b - a + n_a) +'b'+ str(n_c) + 'c' not in d:
                    d[str(a) +'a'+str(n_b - a + n_a) +'b'+ str(n_c) + 'c'] = 1
                    q.append([a,n_b - a + n_a,n_c])
                elif n_b <= a - n_a and str(n_b + n_a) +'a' + str(0) +'b'+ str(n_c) +'c' not in d:
                    d[str(n_b + n_a) +'a' + str(0) +'b'+ str(n_c) +'c'] = 1
                    q.append([n_b + n_a,0,n_c])
            if n_c > 0:
                if n_c >  a - n_a and str(a) +'a'+ str(n_b) + 'b'+ str(n_c - a + n_a) + 'c' not in d:
                    d[str(a) +'a'+ str(n_b) + 'b'+ str(n_c - a + n_a) + 'c'] = 1
                    q.append([a,n_b,n_c - a + n_a])
                elif n_c <=  a - n_a and str(n_c + n_a) + 'a' + str(n_b) +'b'+ str(0)+'c' not in d:
                    d[str(n_c + n_a) + 'a' + str(n_b) +'b'+ str(0)+'c'] = 1
                    q.append([n_c + n_a, n_b ,0])                
        if i == 1:
            if n_a > 0:
                if n_a > b - n_b and str(n_a - b + n_b) +'a' + str(b) +'b'+ str(n_c) +'c' not in d:
                    d[str(n_a - b + n_b) +'a' + str(b) +'b'+ str(n_c) +'c'] = 1
                    q.append([n_a - b + n_b, b, n_c])
                elif n_a <= b - n_b and str(0) +'a'+ str(n_a + n_b) +'b'+ str(n_c) + 'c' not in d:
                    d[str(0) +'a'+ str(n_a + n_b) +'b'+ str(n_c) + 'c'] = 1
                    q.append([0 ,n_a + n_b,n_c])
            if n_c > 0:
                if n_c > b - n_b and str(n_a) + 'a' + str(b) + 'b' + str(n_c - b + n_b) +'c' not in d:
                    d[str(n_a) + 'a' + str(b) + 'b' + str(n_c - b + n_b) +'c'] = 1
                    q.append([n_a , b, n_c - b + n_b])
                elif n_c <=  b - n_b and str(n_a) +'a'+ str(n_b + n_c) +'b'+ str(0) +'c' not in d:
                    d[str(n_a) +'a'+ str(n_b + n_c) +'b'+ str(0) +'c'] = 1
                    q.append([n_a, n_b + n_c ,0])  
        if i == 2:
            if n_a > 0:
                if n_a > c - n_c and str(n_a - c + n_c) +'a' + str(n_b) +'b'+  str(c) +'c' not in d:
                    d[str(n_a - c + n_c) +'a' + str(n_b) +'b'+  str(c) +'c'] = 1
                    q.append([n_a - c + n_c, n_b, c])
                elif n_a <= c - n_c and str(0) +'a'+ str(n_b) +'b'+ str(n_c + n_a) + 'c' not in d:
                    d[str(0) +'a'+ str(n_b) +'b'+ str(n_c + n_a) + 'c'] = 1
                    q.append([0, n_b, n_c + n_a])
            if n_b > 0:
                if n_b >  c - n_c and str(n_a) +'a'+ str(n_b - c + n_c) +'b'+ str(c)+'c' not in d:
                    d[str(n_a) +'a'+ str(n_b - c + n_c) +'b'+ str(c)+'c'] = 1
                    q.append([n_a, n_b - c + n_c, c])
                elif n_b <=  c - n_c and str(n_a) +'a'+  str(0) +'b'+ str(n_b + n_c)+'c' not in d:
                    d[str(n_a) +'a'+  str(0) +'b'+ str(n_b + n_c)+'c'] = 1
                    q.append([n_a, 0 , n_b + n_c])  

answer = sorted(answer)

for i in answer:
    print(i, end = ' ')
