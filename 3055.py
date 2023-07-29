from collections import deque
move = [(0,1), (0,-1), (1,0), (-1,0)]
r, c = map(int,input().split())
data = [input() for _ in range(r)]
water = deque()
gosim = deque()
water_v = [[-1] * c for _ in range(r)]
gosim_v = [[-1] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if data[i][j] == 'S':
            gosim.append([i,j])
            gosim_v[i][j] = 0
        if data[i][j] == '*':
            water.append([i,j])
            water_v[i][j] = 0
        if data[i][j] == 'D':
            goal = [i,j]

while water:
    y,x = water.popleft()
    for i,j in move:
        if 0 <= y+i < r and 0 <= x+j < c and data[y+i][x+j] != 'D' and data[y+i][x+j] != 'X' and water_v[y+i][x+j] == -1:
            water_v[y+i][x+j] = water_v[y][x] + 1
            water.append([y+i,x+j])
            
while gosim:
    y,x = gosim.popleft()
    if y == goal[0] and x == goal[1]:
        print(gosim_v[y][x])
        exit()
    for i,j in move:
        if 0 <= y+i < r and 0 <= x+j < c and data[y+i][x+j] != '*' and data[y+i][x+j] != 'X' and gosim_v[y+i][x+j] == -1 and (water_v[y+i][x+j] == -1 or water_v[y+i][x+j] > gosim_v[y][x] + 1):
            gosim_v[y+i][x+j] = gosim_v[y][x] + 1
            gosim.append([y+i,x+j])

print("KAKTUS")