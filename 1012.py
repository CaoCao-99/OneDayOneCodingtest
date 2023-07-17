move = [(0,1), (0,-1), (1,0), (-1,0)]

def DFS(y,x,l_y, l_x, tile):
    for a,b in move:
        if 0 <= y+a < l_y and 0<= x + b <l_x:
            if tile[y+a][x+b] == 1:
                tile[y+a][x+b] = 0
                DFS(y+a, x+b, l_y, l_x, tile)
#tile이 잘 넘어가는지 확인(전역변수 취급?)

case_num = int(input())
real_answer = []

for i in range(case_num):
    x,y,num = map(int,input().split())
    cabbage_map = [[0 for i in range(x)] for j in range(y)]
    for j in range(num):
        a,b = map(int,input().split())
        cabbage_map[b][a] = 1
    answer = 0
    for a in range(y):
        for b in range(x):
            if cabbage_map[a][b] == 1:
                cabbage_map[a][b] = 0
                DFS(a,b,y,x, cabbage_map)
                answer+=1
    real_answer.append(answer)

for i in real_answer:
    print(i)