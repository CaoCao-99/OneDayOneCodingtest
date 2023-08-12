import copy
data = list(map(int, input().split()))
normal_map = list(range(0,41,2))
normal_map.append(0)
special_map1 = [10,13,16,19,25,30,35,40,0]
special_map2 = [20,22,24,25,30,35,40,0]
special_map3 = [30,28,27,26,25,30,35,40,0]
horse = [[0, 0],[0, 0],[0, 0],[0, 0]] #말이 속한 맵, 말이 속한 맵안에서의 위치(인덱스)
visit = dict()
visit['00000000'] = True
answer = 0


def get_func(num):
    if num == 0:
        return normal_map
    elif num == 1:
        return special_map1
    elif num == 2:
        return special_map2
    else: 
        return special_map3




def rec(horse, cnt, ans, visit): #현재 말이 어떤 map에 있는지 표현, 현재 진행한 횟수, 현재까지 오는데 얻은 포인트
    global answer
    if cnt == 10:
        answer = max(answer, ans)
        return
    for i in range(4): 
        new_horse = copy.deepcopy(horse)
        now_map = get_func(new_horse[i][0])
        if new_horse[i][1] < len(now_map) - 1:
            if now_map[new_horse[i][1]] == 10 and new_horse[i][0] == 0:
                new_horse[i][0] = 1
                new_horse[i][1] = data[cnt]
                v=''
                aa = []
                for j in range(4):
                    v += str(new_horse[j][0]) + str(new_horse[j][1])
                    if i != j:
                        aa.append(str(new_horse[j][0]) + str(new_horse[j][1]))
                    
                if v in visit or str(new_horse[i][0]) + str(new_horse[i][1]) in aa:
                    continue
                else:
                    visit[v] = True
                    rec(new_horse, cnt + 1, ans + special_map1[new_horse[i][1]], visit)
                    del visit[v]
                
            elif now_map[new_horse[i][1]] == 20 and new_horse[i][0] == 0:
                new_horse[i][0] = 2
                new_horse[i][1] = data[cnt]
                v=''
                aa = []
                for j in range(4):
                    v += str(new_horse[j][0]) + str(new_horse[j][1])
                    if i != j:
                        aa.append(str(new_horse[j][0]) + str(new_horse[j][1]))
                    
                if v in visit or str(new_horse[i][0]) + str(new_horse[i][1]) in aa:
                    continue
                else:
                    visit[v] = True
                    rec(new_horse, cnt + 1, ans + special_map2[new_horse[i][1]], visit)
                    del visit[v]

                
            elif now_map[new_horse[i][1]] == 30 and new_horse[i][0] == 0:
                new_horse[i][0] = 3
                new_horse[i][1] = data[cnt]
                v=''
                aa = []
                for j in range(4):
                    v += str(new_horse[j][0]) + str(new_horse[j][1])
                    if i != j:
                        aa.append(str(new_horse[j][0]) + str(new_horse[j][1]))
                    
                if v in visit or str(new_horse[i][0]) + str(new_horse[i][1]) in aa:
                    continue
                else:
                    visit[v] = True
                    rec(new_horse, cnt + 1, ans + special_map3[new_horse[i][1]], visit)
                    del visit[v]
            
            else:
                next = min(len(now_map) - 1,new_horse[i][1] + data[cnt])
                new_horse[i][1] = next
                v=''
                aa = []
                for j in range(4):
                    v += str(new_horse[j][0]) + str(new_horse[j][1])
                    if i != j:
                        aa.append(str(new_horse[j][0]) + str(new_horse[j][1]))
                    
                if v in visit or (now_map[next] != 0 and str(new_horse[i][0]) + str(new_horse[i][1]) in aa):
                    continue
                else:
                    visit[v] = True
                    rec(new_horse, cnt + 1, ans + now_map[next], visit)
                    del visit[v]


rec(horse, 0, 0, visit)
print(answer)