import heapq
q = []
move = [(0,1), (0,-1), (1,0), (-1,0)]
n, m = map(int,input().split())
y1,x1,y2,x2 = map(int,input().split())
y1-=1
x1-=1
y2-=1
x2-=1
data = [input() for i in range(n)]
heapq.heappush(q, (1,(y1, x1)))         #(cnt, (y1, x1))
visit = [[False for _ in range(m)]for _ in range(n)]
visit[y1][x1] = True

while q:
    cnt, pos = heapq.heappop(q)
    y,x = pos[0],pos[1]
    if y == y2 and x == x2:
        print(cnt)
        exit()
    for i,j in move:
        if 0 <= y+i < n and 0 <= x+j < m and visit[y+i][x+j] == False:
            visit[y+i][x+j] = True
            if data[y+i][x+j] == '1':
                heapq.heappush(q, (cnt+1, (y+i, x+j)))
            else:
                heapq.heappush(q, (cnt, (y+i, x+j)))
                

