from collections import deque
n,m = map(int,input().split())
r,c,look = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
move = [(-1,0), (0,1), (1,0), (0,-1)]
answer = 1

def detect(y,x,l):
    for i in range(4):
        l = (l+3)%4
        n_y = y + move[l][0]
        n_x = x + move[l][1]
        if 0 <= n_y < n and 0 <= n_x < m and data[n_y][n_x] == 0:
            return [n_y, n_x, l]
    return 0



q = deque()
q.append([r,c,look])
data[r][c] = 2
while q:
    y,x,l = q.popleft()
    a = detect(y,x,l)
    if a == 0:
        back = move[(l+2)%4]
        if y+back[0] <0 or n <= y + back[0] or x+back[1] <0 or m <= x+back[1] or data[y+back[0]][x+back[1]] == 1:
            print(answer)
            exit()
        else:
            q.append([y+back[0], x+back[1],l])            
    else:
        z,w,e = a
        answer += 1
        data[z][w] = 2
        q.append([z,w,e])


        
        
