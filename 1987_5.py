import sys
import copy
from collections import deque
input = sys.stdin.readline
r, c = map(int,input().split())
data = [input() for _ in range(r)]
move = [(0,1), (0,-1), (-1,0), (1,0)]
q = set([(0,0, data[0][0], 1)])
answer = 0
while q:
    y,x,visit,cnt = q.pop()
    answer = max(answer, cnt)
    for i,j in move:
        if 0 <= y+i < r and 0 <= x+j <c and  data[y+i][x+j] not in visit:
            q.add((y+i, x+j, visit + data[y+i][x+j], cnt + 1))
print(answer)



