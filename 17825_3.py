import copy
data = list(map(int, input().split()))
normal_map = list(range(0,41,2))
normal_map.append(0)
print(normal_map)
print(len(normal_map))
special_map1 = [10,13,16,19,25,30,35,40,0]
special_map2 = [20,22,24,25,30,35,40,0]
special_map3 = [30,28,27,26,25,30,35,40,0]
horse = [[0, 0],[0, 0],[0, 0],[0, 0]] #말이 속한 맵, 말이 속한 맵안에서의 위치(인덱스)
answer = 0


def get_func(num):
    if num == 0:
        return normal_map
    elif num == 1:
        return special_map1
    elif num == 2:
        return special_map2
    elif num == 3: 
        return special_map3




def rec(horse, cnt, ans): #현재 말이 어떤 map에 있는지 표현, 현재 진행한 횟수, 현재까지 오는데 얻은 포인트
    global answer
    if cnt == 10:
        answer = max(answer, ans)
        return
    new_horse = copy.deepcopy(horse)
    for i in range(4): 
        now_map = get_func(horse[i][0])
        if new_horse[i][1] < len(now_map) - 1:
            if now_map[new_horse[i][1]] == 10 and new_horse[i][0] == 0:
                b_i = 0
                b_j = new_horse[i][1]
                new_horse[i][0] = 1
                new_horse[i][1] = data[cnt]
                if [new_horse[i][0], new_horse[i][1]] in horse:
                    new_horse[i] = [b_i,b_j]
                    continue
                if new_horse[i][1] >= 4:
                    if [2,new_horse[i][1]-1] in horse or [3,new_horse[i][1]] in horse:
                        new_horse[i] = [b_i,b_j]
                        continue
                else:
                    rec(new_horse, cnt + 1, ans + special_map1[new_horse[i][1]])
                    new_horse[i] = [b_i,b_j]

            elif now_map[new_horse[i][1]] == 20 and new_horse[i][0] == 0:
                b_i = 0
                b_j = new_horse[i][1]
                new_horse[i][0] = 2
                new_horse[i][1] = data[cnt]
                if [new_horse[i][0], new_horse[i][1]] in horse:
                    new_horse[i] = [b_i,b_j]
                    continue
                if new_horse[i][1] >= 3:
                    if [1,new_horse[i][1]+1] in horse or [3,new_horse[i][1] + 1] in horse:
                        new_horse[i] = [b_i,b_j]
                        continue
                else:
                    rec(new_horse, cnt + 1, ans + special_map2[new_horse[i][1]])
                    new_horse[i] = [b_i,b_j]
 
            elif now_map[new_horse[i][1]] == 30 and new_horse[i][0] == 0:
                b_i = 0
                b_j = new_horse[i][1]
                new_horse[i][0] = 3
                new_horse[i][1] = data[cnt]
                if [new_horse[i][0], new_horse[i][1]] in horse:
                    new_horse[i] = [b_i,b_j]
                    continue
                if new_horse[i][1] >= 4:
                    if [2,new_horse[i][1]-1] in horse or [1,new_horse[i][1]] in horse:
                        new_horse[i] = [b_i,b_j]
                        continue
                else:
                    rec(new_horse, cnt + 1, ans + special_map3[new_horse[i][1]])
                    new_horse[i] = [b_i,b_j]
            
            else:
                next = min(len(now_map) - 1,new_horse[i][1] + data[cnt])
                b_i = new_horse[i][0]
                b_j = new_horse[i][1]
                new_horse[i][1] = next
                if [new_horse[i][0], new_horse[i][1]] in horse and next != len(now_map) - 1:
                    new_horse[i] = [b_i,b_j]
                    continue
                if new_horse[i][0] == 1:
                    if new_horse[i][1] >= 4 and new_horse[i][1] != len(now_map) - 1:
                        if [2,new_horse[i][1]-1] in horse or [3,new_horse[i][1]] in horse:
                            new_horse[i] = [b_i,b_j]
                            continue
                if new_horse[i][0] == 2:
                    if new_horse[i][1] >= 3 and new_horse[i][1] != len(now_map) - 1:
                        if [1,new_horse[i][1]+1] in horse or [3,new_horse[i][1] + 1] in horse:
                            new_horse[i] = [b_i,b_j]
                            continue
                if new_horse[i][0] == 3:
                    if new_horse[i][1] >= 4 and new_horse[i][1] != len(now_map) - 1:
                        if [2,new_horse[i][1]-1] in horse or [1,new_horse[i][1]] in horse:
                            new_horse[i] = [b_i,b_j]
                            continue
                else:
                    rec(new_horse, cnt + 1, ans + now_map[next])
                    new_horse[i] = [b_i,b_j]



rec(horse, 0, 0)
print(answer)