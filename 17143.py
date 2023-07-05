r,c,m = map(int,input().split())
a = list()
q = list()
grid = [[None, None, None] * (c+1) for _ in range(r+1)]

for i in range(m):
    z,x,zz,v,b = map(int,input().split())
    a.append(i)
    grid[z][x] = [zz,v,b]


answer = 0


for i in range(1,c+1):
    #잡기
    for j in range(1,r+1):
        if grid[j][i] != None:
            answer += grid[j][i][2]
            grid[j][i] = None
            break

    #이동시킬(후) 공간 만들기
    moved_grid = [[None, None, None] * (c+1) for _ in range(r+1)]

    #이동 시키기
    for a in range(1, r+1):
        for b in range(1, c+1):
            if grid[a][b] != None:
                y,x= a,b
                move_lim = grid[a][b][0]
                #상 / 하
                if grid[a][b][1] == 1:
                    if move_lim<=(a-1):
                        if moved_grid[a-move_lim][b] == None:
                            moved_grid[a-move_lim][b] = grid[a][b]
                        else:
                            if moved_grid[a-move_lim][b][2] > grid[a][b][2]:
                                continue
                            else:
                                moved_grid[a-move_lim][b] = grid[a][b]

                    if move_lim > (a-1):
                        move_lim-=a-1
                        y=1
                        grid[a][b][1] = 2
                        if (move_lim//(r-1))%2 == 0:
                            if  moved_grid[1+move_lim%(r-1)][b] == None:
                                moved_grid[1+move_lim%(r-1)][b] = grid[a][b]
                            else:
                                if moved_grid[1+move_lim%(r-1)][b][2]  > grid[a][b][2]:
                                    continue
                                else:
                                    moved_grid[1+move_lim%(r-1)][b] = grid[a][b]
                        else:
                            grid[a][b][1] = 1
                            if moved_grid[r-move_lim%(r-1)][b] == None:                                
                                moved_grid[r-move_lim%(r-1)][b] = grid[a][b]
                            else:
                                if moved_grid[r-move_lim%(r-1)][b][2] > grid[a][b][2]:
                                    continue
                                else:
                                    moved_grid[r-move_lim%(r-1)][b] = grid[a][b]
                
                elif grid[a][b][1] == 2:
                    if move_lim<=(r-a):
                        if moved_grid[a+move_lim][b] == None:
                            moved_grid[a+move_lim][b] = grid[a][b]
                        elif moved_grid[a+move_lim][b][2] > grid[a][b][2] :
                            continue
                        else:
                            moved_grid[a+move_lim][b] = grid[a][b]
                    if move_lim > (r-a):
                        move_lim-=r-a
                        y=r
                        grid[a][b][1] = 1
                        if (move_lim//(r-1))%2 == 0:
                            if moved_grid[r - move_lim%(r-1)][b] ==None:
                                moved_grid[r - move_lim%(r-1)][b] = grid[a][b]
                            elif moved_grid[r - move_lim%(r-1)][b][2] > grid[a][b][2]:
                                continue
                            else:
                                moved_grid[r - move_lim%(r-1)][b] = grid[a][b]
                        else:
                            grid[a][b][1] = 2
                            if moved_grid[1+move_lim%(r-1)][b] == None:                    
                                moved_grid[1+move_lim%(r-1)][b] = grid[a][b]
                            elif moved_grid[1+move_lim%(r-1)][b][2] > grid[a][b][2]:
                                continue
                            else:
                                moved_grid[1+move_lim%(r-1)][b] = grid[a][b]
                
                #좌 / 우
                elif grid[a][b][1] == 4:
                    if move_lim<=(b-1):
                        if moved_grid[a][b - move_lim] == None:
                            moved_grid[a][b - move_lim] = grid[a][b]
                        elif moved_grid[a][b - move_lim][2] > grid[a][b][2]:
                            continue
                        else: 
                            moved_grid[a][b - move_lim] = grid[a][b]
                    if move_lim > (b-1):
                        move_lim-=b-1
                        x=1
                        grid[a][b][1] = 3
                        if (move_lim//(c-1))%2 == 0:
                            if moved_grid[a][1+move_lim%(c-1)] == None:
                                moved_grid[a][1+move_lim%(c-1)] = grid[a][b]
                            elif moved_grid[a][1+move_lim%(c-1)][2] > grid[a][b][2]:
                                continue
                            else:
                                moved_grid[a][1+move_lim%(c-1)] = grid[a][b]
                        else:
                            grid[a][b][1] = 4
                            if moved_grid[a][c-move_lim%(c-1)] == None:                        
                                moved_grid[a][c-move_lim%(c-1)] = grid[a][b]
                            elif moved_grid[a][c-move_lim%(c-1)][2] > grid[a][b][2]:
                                continue
                            else:
                                moved_grid[a][c-move_lim%(c-1)] = grid[a][b]
                
                elif grid[a][b][1] == 3:
                    if move_lim<=(c-b):
                        if moved_grid[a][b+move_lim] == None:
                            moved_grid[a][b+move_lim] = grid[a][b]
                        elif moved_grid[a][b+move_lim][2] > grid[a][b][2]:
                            continue
                        else:
                            moved_grid[a][b+move_lim] = grid[a][b]
                    if move_lim > (c-b):
                        move_lim-=c-b
                        x=c
                        grid[a][b][1] = 4
                        if (move_lim//(c-1))%2 == 0:
                            if moved_grid[a][c - move_lim%(c-1)] == None:
                                moved_grid[a][c - move_lim%(c-1)] = grid[a][b]
                            elif moved_grid[a][c - move_lim%(c-1)][2] > grid[a][b][2]:
                                continue
                            else:
                                moved_grid[a][c - move_lim%(c-1)] = grid[a][b]
                        else:
                            grid[a][b][1] = 3
                            if  moved_grid[a][1+move_lim%(c-1)] == None:
                                moved_grid[a][1+move_lim%(c-1)] = grid[a][b]
                            elif  moved_grid[a][1+move_lim%(c-1)][2] > grid[a][b][2]:
                                continue
                            else:
                                 moved_grid[a][1+move_lim%(c-1)] = grid[a][b]

    grid = moved_grid  
print(answer)
        
            