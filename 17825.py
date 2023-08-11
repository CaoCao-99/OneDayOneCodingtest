import copy
data = list(map(int, input().split()))
normal_map = range(0,41,2)
special_map1 = [10,13,16,19,25,30,35,40]
special_map2 = [20,22,24,25,30,35,40]
special_map3 = [30,28,27,26,25,30,35,40]
horse = [[normal_map, 0],[normal_map, 0],[normal_map, 0],[normal_map, 0]] #말이 속한 맵, 말이 속한 맵안에서의 위치(인덱스)
visit = dict()
visit['00000000'] = True
answer = 0
def rec(horse, cnt, ans, visit): #현재 말이 어떤 map에 있는지 표현, 현재 진행한 횟수, 현재까지 오는데 얻은 포인트
    global answer
    if cnt == 10:
        answer = max(answer, ans)
        return

    h1,h2,h3,h4 = horse[0],horse[1],horse[2],horse[3]
    v = str(h1[:]) + str(h2[:]) + str(h3[:]) + str(h4[:])


    for i in range(4): 
        new_horse = copy.deepcopy(horse)
        if new_horse[i][1] < len(new_horse[i][0]):
            if new_horse[i][0][new_horse[i][1]] == 10:
                new_horse[i][0] = special_map1
                new_horse[i][1] = data[cnt]
                v=''
                for j in range(4):
                    v += str(new_horse[i][0]) + str(new_horse[i][1])
                if v in visit:
                    continue
                else:
                    visit[v] = True
                    rec(new_horse, cnt + 1, ans + special_map1[new_horse[i][1]], visit)
                  #  del visit[v]
                
            elif new_horse[i][0][new_horse[i][1]] == 20:
                new_horse[i][0] = special_map2
                new_horse[i][1] = data[cnt]
                v=''
                for j in range(4):
                    v += str(new_horse[i][0]) + str(new_horse[i][1])
                if v in visit:
                    continue
                else:
                    visit[v] = True
                    rec(new_horse, cnt + 1, ans + special_map2[new_horse[i][1]], visit)
                    #del visit[v]

                
            elif new_horse[i][0][new_horse[i][1]] == 30:
                new_horse[i][0] = special_map3
                new_horse[i][1] = data[cnt]
                v=''
                for j in range(4):
                    v += str(new_horse[i][0]) + str(new_horse[i][1])
                if v in visit:
                    continue
                else:
                    visit[v] = True
                    rec(new_horse, cnt + 1, ans + special_map3[new_horse[i][1]], visit)
                    #del visit[v]
            
            else:
                next = min(len(new_horse[i][0]) - 1,new_horse[i][1] + data[cnt])
                new_horse[i][1] = next
                v=''
                for j in range(4):
                    v += str(new_horse[i][0]) + str(new_horse[i][1])
                if v in visit:
                    continue
                else:
                    visit[v] = True
                    rec(new_horse, cnt + 1, ans + new_horse[i][0][next], visit)
                    #del visit[v]


rec(horse, 0, 0, visit)
print(answer)