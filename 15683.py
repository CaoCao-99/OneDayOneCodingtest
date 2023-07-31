import copy
move = [(-1,0), (0,1), (1,0), (0,-1)]
def check(i):
    if cctv[i][2] == 1:
        return [[0],[1],[2],[3]]
    elif cctv[i][2] == 2:
        return [[0,2], [1,3]]
    elif cctv[i][2] == 3:
        return [[0,1],[1,2],[2,3],[3,0]]
    elif cctv[i][2] == 4:
        return [[0,1,2],[1,2,3], [2,3,0],[3,0,1]]
    else:
        return [[0,1,2,3]]

def rec(data, now):
    global answer
    if now == len(cctv):
        a = 0
        for i in range(n):
            a += data[i].count(0)
        answer = min(answer, a)        
        return
    else:
        new_data = copy.deepcopy(data)
        y,x,num = cctv[now]
        for dir in check(now):
            dfs(y,x,dir,new_data)
            rec(new_data, now+1)
            new_data = copy.deepcopy(data)


def dfs(y,x,dir,data):
    for way in dir:
        n_y, n_x = y,x
        while True:
            n_y += move[way][0]
            n_x += move[way][1]
            if 0 <= n_y < n and 0 <= n_x < m:
                if data[n_y][n_x] == 6:
                    break
                elif data[n_y][n_x] == 0:
                    data[n_y][n_x] = 7
            else:
                break




    

n, m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if data[i][j] != 0 and data[i][j] != 6:
            cctv.append([i,j,data[i][j]])
answer = 10000000000000
rec(data,0)
print(answer)

# every = []
# new_list = []
# for a in range(len(cctv)):
#     for a1 in check(a):
#         first = a1
#         for b in range(a+1, len(cctv)):
#             for b1 in check(b):
#                 second = b1
#                 for c in range(b+1, len(cctv)):
#                     for c1 in check(c):
#                         third = c1
#                         for d in range(c+1, len(cctv)):
#                             for d1 in check(d):
#                                 fourth = d1
#                                 for e in range(d+1, len(cctv)):
#                                     for e1 in check(e):
#                                         fifth = d1

        
# 0 , 1, 2, 3, [1,2]

