n = int(input())
field = []


def rec(now, cnt, past):
    if now >= n:
        cnt += 1
        return cnt
    if now+1 <=n:
        cnt = rec(now+1,cnt,0)
    if now + 2 <=n:
        cnt = rec(now+2,cnt, 1)
        cnt = rec(now+2,cnt, 2)  
      
    return cnt

if n == 1:
    print(1)
    exit()

answer = rec(1,0,0) + rec(2,0,1) + rec(2,0,2)
print(answer)