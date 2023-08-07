import sys
import copy
from collections import deque
input = sys.stdin.readline
r, c = map(int,input().split())
data = [input() for _ in range(r)]
move = [(0,1), (0,-1), (-1,0), (1,0)]
q = deque()
q.append([0,0,set(data[0][0]),1])
answer = 0
while q:
    y,x,visit,cnt = q.pop()
    answer = max(answer, cnt)
    for i,j in move:
        new_visit = copy.deepcopy(visit)
        if 0 <= y+i < r and 0 <= x+j <c and not data[y+i][x+j] in new_visit:
            new_visit.add(data[y+i][x+j])
            q.append([y+i, x+j, new_visit, cnt + 1])
print(answer)



