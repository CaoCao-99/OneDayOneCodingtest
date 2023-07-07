n,k = map(int,input().split()) #0~n-1
field_map = []
#horse_num = 0~k-1

for i in range(n):
    field_map.append(list(map(int,input().split())))

#horse_map = [[[]] * n for i in range(n)] # (2,3) = 1,2,3 == 1,2,3번 말이 (2,3)에 존재
horse_map = [[[] for _ in range(n)] for _ in range(n)]
horse_dir = []
horse_pos = [(0,0)] * k 


for i in range(k):
    a,b,c = map(int,input().split())
    horse_map[a-1][b-1].append(i)
    #print(horse_map[a-1][b-1])
    horse_dir.append(c)
    horse_pos[i] = (a-1,b-1)


for term in range(1000):
    #말을 순서대로 이동시키기
    for i in range(k):#horse_num
        pos_y, pos_x = horse_pos[i]
        start = horse_map[pos_y][pos_x].index(i)
        horse_length = len(horse_map[pos_y][pos_x])
        if horse_dir[i] == 1: #우측
            #다음칸이 파란색이거나 경로가 없을 경우
            if pos_x+1 >= n or field_map[pos_y][pos_x+1] == 2:
                # for h_num in range(start,horse_length):
                #     horse_dir[h_num] = 2
                horse_dir[horse_map[pos_y][pos_x][start]]=2
                #반대칸이 파란색인 경우(아무것도 하지 않음)
                if pos_x-1 < 0 or field_map[pos_y][pos_x-1] == 2:
                    continue
                else:
                    #흰칸 or 빨강일 때
                    if field_map[pos_y][pos_x-1] == 0:#흰칸인 경우
                            
                        for in_horse in range(start, horse_length):
                            horse_map[pos_y][pos_x-1].append(horse_map[pos_y][pos_x][in_horse])
        #                            horse_map[pos_y][pos_x].pop(start)
                            horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x-1)
                            #horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x-1)

                    elif field_map[pos_y][pos_x-1] == 1:#빨강인 경우
                        aa = horse_map[pos_y][pos_x][start: horse_length]
                        if aa != None:
                            aa = aa[::-1]
                            #horse_map[pos_y][pos_x-1].append(aa)
                            for xxxx in aa :
                                horse_map[pos_y][pos_x-1].append(xxxx)
                                horse_pos[xxxx] = (pos_y,pos_x-1)
                    del horse_map[pos_y][pos_x][start:horse_length]
                

            else:
                    #흰칸 or 빨강일 때
                    if field_map[pos_y][pos_x+1] == 0:#흰칸인 경우
                            
                        for in_horse in range(start, horse_length):
                            horse_map[pos_y][pos_x+1].append(horse_map[pos_y][pos_x][in_horse])
        #                            horse_map[pos_y][pos_x].pop(start)
                            horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x+1)
                            #horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x-1)

                    elif field_map[pos_y][pos_x+1] == 1:#빨강인 경우
                        aa = horse_map[pos_y][pos_x][start: horse_length]
                        if aa != None:
                            aa = aa[::-1]
                            for xxxx in aa :
                                horse_map[pos_y][pos_x+1].append(xxxx)
                                horse_pos[xxxx] = (pos_y,pos_x+1)
                    del horse_map[pos_y][pos_x][start:horse_length]

                    
        elif horse_dir[i] == 2: #좌측
            #다음칸이 파란색이거나 경로가 없을 경우
            if pos_x-1 < 0 or field_map[pos_y][pos_x-1] == 2:
                # for h_num in range(start,horse_length):
                #     horse_dir[h_num] = 1
                horse_dir[horse_map[pos_y][pos_x][start]] = 1
                #반대칸이 파란색인 경우(아무것도 하지 않음)
                if pos_x+1 >= n or field_map[pos_y][pos_x+1] == 2:
                    continue
                else:
                                       #흰칸 or 빨강일 때
                    if field_map[pos_y][pos_x+1] == 0:#흰칸인 경우
                            
                        for in_horse in range(start, horse_length):
                            horse_map[pos_y][pos_x+1].append(horse_map[pos_y][pos_x][in_horse])
        #                            horse_map[pos_y][pos_x].pop(start)
                            horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x+1)
                            #horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x-1)

                    elif field_map[pos_y][pos_x+1] == 1:#빨강인 경우
                        aa = horse_map[pos_y][pos_x][start: horse_length]
                        if aa != None:
                            aa = aa[::-1]
                            for xxxx in aa :
                                horse_map[pos_y][pos_x+1].append(xxxx)
                                horse_pos[xxxx] = (pos_y,pos_x+1)
                    del horse_map[pos_y][pos_x][start:horse_length]
            else:    
                                #흰칸 or 빨강일 때
                if field_map[pos_y][pos_x-1] == 0:#흰칸인 경우
                        
                    for in_horse in range(start, horse_length):
                        horse_map[pos_y][pos_x-1].append(horse_map[pos_y][pos_x][in_horse])
    #                            horse_map[pos_y][pos_x].pop(start)
                        horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x-1)
                        #horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x-1)

                elif field_map[pos_y][pos_x-1] == 1:#빨강인 경우
                    aa = horse_map[pos_y][pos_x][start: horse_length]
                    if aa != None:
                        aa = aa[::-1]
                        for xxxx in aa :
                            horse_map[pos_y][pos_x-1].append(xxxx)
                            horse_pos[xxxx] = (pos_y,pos_x-1)
                del horse_map[pos_y][pos_x][start:horse_length]
                
        
        
        elif horse_dir[i] == 3: #상단
                       #다음칸이 파란색이거나 경로가 없을 경우
            if pos_y-1 < 0 or field_map[pos_y-1][pos_x] == 2:
                # for h_num in range(start,horse_length):
                #     horse_dir[h_num] = 4
                horse_dir[horse_map[pos_y][pos_x][start]] = 4
                #반대칸이 파란색인 경우(아무것도 하지 않음)
                if pos_y+1 >=n or field_map[pos_y+1][pos_x] == 2:
                    continue
                else:
                                       #흰칸 or 빨강일 때
                    if field_map[pos_y+1][pos_x] == 0:#흰칸인 경우
                            
                        for in_horse in range(start, horse_length):
                            horse_map[pos_y+1][pos_x].append(horse_map[pos_y][pos_x][in_horse])
        #                            horse_map[pos_y][pos_x].pop(start)
                            horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y+1, pos_x)
                            #horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x-1)

                    elif field_map[pos_y+1][pos_x] == 1:#빨강인 경우
                        aa = horse_map[pos_y][pos_x][start: horse_length]
                        if aa != None:
                            aa = aa[::-1]
                            for xxxx in aa :
                                horse_map[pos_y+1][pos_x].append(xxxx)
                                horse_pos[xxxx] = (pos_y+1,pos_x)
                    del horse_map[pos_y][pos_x][start:horse_length]
            else:    
                                                    #흰칸 or 빨강일 때
                if field_map[pos_y-1][pos_x] == 0:#흰칸인 경우
                        
                    for in_horse in range(start, horse_length):
                        horse_map[pos_y-1][pos_x].append(horse_map[pos_y][pos_x][in_horse])
    #                            horse_map[pos_y][pos_x].pop(start)
                        horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y-1, pos_x)
                        #horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x-1)

                elif field_map[pos_y-1][pos_x] == 1:#빨강인 경우
                    aa = horse_map[pos_y][pos_x][start: horse_length]
                    if aa != None:
                        aa = aa[::-1]
                        for xxxx in aa :
                            horse_map[pos_y-1][pos_x].append(xxxx)
                            horse_pos[xxxx] = (pos_y-1,pos_x)
                del horse_map[pos_y][pos_x][start:horse_length]
         
                
        
        elif horse_dir[i] == 4: #하단
                      #다음칸이 파란색이거나 경로가 없을 경우
            if pos_y+1 >= n or field_map[pos_y+1][pos_x] == 2:
                # for h_num in range(start,horse_length):
                #     horse_dir[h_num] = 3
                horse_dir[horse_map[pos_y][pos_x][start]] = 3
                #반대칸이 파란색인 경우(아무것도 하지 않음)
                if pos_y - 1 < 0 or field_map[pos_y-1][pos_x] == 2:
                    continue
                else:
                                                                        #흰칸 or 빨강일 때
                    if field_map[pos_y-1][pos_x] == 0:#흰칸인 경우
                            
                        for in_horse in range(start, horse_length):
                            horse_map[pos_y-1][pos_x].append(horse_map[pos_y][pos_x][in_horse])
        #                            horse_map[pos_y][pos_x].pop(start)
                            horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y-1, pos_x)
                            #horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x-1)

                    elif field_map[pos_y-1][pos_x] == 1:#빨강인 경우
                        aa = horse_map[pos_y][pos_x][start: horse_length]
                        if aa != None:
                            aa = aa[::-1]
                            for xxxx in aa :
                                horse_map[pos_y-1][pos_x].append(xxxx)
                                horse_pos[xxxx] = (pos_y-1,pos_x)
                    del horse_map[pos_y][pos_x][start:horse_length]
            
                    
            else:
                #흰칸 or 빨강일 때
                                #흰칸 or 빨강일 때
                if field_map[pos_y+1][pos_x] == 0:#흰칸인 경우
                        
                    for in_horse in range(start, horse_length):
                        horse_map[pos_y+1][pos_x].append(horse_map[pos_y][pos_x][in_horse])
    #                            horse_map[pos_y][pos_x].pop(start)
                        horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y+1, pos_x)
                        #horse_pos[horse_map[pos_y][pos_x][in_horse]] = (pos_y, pos_x-1)

                elif field_map[pos_y+1][pos_x] == 1:#빨강인 경우
                    aa = horse_map[pos_y][pos_x][start: horse_length]
                    if aa != None:
                        aa = aa[::-1]
                        for xxxx in aa :
                            horse_map[pos_y+1][pos_x].append(xxxx)
                            horse_pos[xxxx] = (pos_y+1,pos_x)
                del horse_map[pos_y][pos_x][start:horse_length]
                    

        #조건을 만족했을 경우
        for i in range(n):
            #print(horse_map[i])
            for j in range(n):
                if horse_map[i][j] != None and len(horse_map[i][j]) >=4 :
                    print(term+1)
                    exit()

print(-1)

