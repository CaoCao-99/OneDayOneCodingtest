b, a = map(int,input().split())
data = list(map(int,input().split()))
move = [(0,1)]
tile = [[0 for j in range(a)] for i in range(b)]
visit = [[0 for j in range(a)] for i in range(b)]

def DFS(y,x,cnt):
    if x+1 >= a:#범위를 넘어간경우
        return 0
    
    if tile[y][x+1] == 0:
        visit[y][x+1] = 1
        cnt = DFS(y,x+1,cnt+1)
    
    return cnt
    

for i in range(len(data)):
    for j in range(data[i]):
        tile[-(j+1)][i] = 1
    
    
answer = 0
for i in range(b-1,-1,-1):
    for j in range(a):
        if tile[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            answer += DFS(i,j,0)  

print(answer)


