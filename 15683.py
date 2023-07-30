import copy
move = {(-1,0), (0,1), (1,0), (0,-1)}
def check(i):
    if cctv[i][2] == 1:
        return [[0],[1],[2],[3]]
    elif cctv[i][2] == 2:
        return [[0,2], [1,3]]
    elif cctv[i][2] == 3:
        return [[0,1],[1,2],[2,3],[3,0]]
    elif cctv[i][2] == 4:
        return [[0,1,2],[1,2,3][2,3,0],[3,0,1]]
    else:
        return [[0,1,2,3]]

def rec(data, now, answer):
    if now == len(cctv) -1:
        answer = max(answer, count(data))        
        return answer
    else:
        y,x,num = cctv[now]
        for dir in check(num):
            new_data = copy.deepcopy(data)
            dfs(y,x,dir,data)
            rec(new_data, now+1, answer)

def dfs(y,x,dir,data):
    for way in dir:
        n_y, n_x = y,x
        cnt = 0
        while True:
            n_y += move[way][0]
            n_x += move[way][1]
            if 0 <= n_y < n and 0 <= n_x < m:
                if data[n_y][n_x] == 6:
                    break
                elif data[n_y][n_x] == 0:
                    cnt+=1
            else:
                break




    

n, m = map(int,input().split())
data = [list(map(int,input().split()))]
cctv = []
for i in range(n):
    for j in range(m):
        if data[i][j] != 0 and data[i][j] != 6:
            cctv.append([i,j,data[i][j]])

every = []
new_list = []
for a in range(len(cctv)):
    for a1 in check(a):
        first = a1
        for b in range(a+1, len(cctv)):
            for b1 in check(b):
                second = b1
                for c in range(b+1, len(cctv)):
                    for c1 in check(c):
                        third = c1
                        for d in range(c+1, len(cctv)):
                            for d1 in check(d):
                                fourth = d1
                                for e in range(d+1, len(cctv)):
                                    for e1 in check(e):
                                        fifth = d1

        
# 0 , 1, 2, 3, [1,2]

