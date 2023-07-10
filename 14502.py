import itertools
import copy
move = [(1,0), (-1,0), (0,1), (0,-1)]
n , m = map(int,input().split())
b_map = [[0] * m for i in range(n)]
empty_map = []
virus_map = []
#print(map) 
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(len(a)):
        b_map[i][j] = a[j]
        if a[j] == 0:
            empty_map.append((i,j))
        if a[j] == 2:
            virus_map.append((i,j))
brute = list(itertools.combinations(empty_map,3))
ans_list = []
for i in range(len(brute)):
    answer = 0
    a_map =  copy.deepcopy(b_map)
    v_map = copy.deepcopy(virus_map)
    visit = [[0] * m for i in range(n)]
    a,b,c = brute[i]
    #print(brute[i])
    a_map[a[0]][a[1]] = 1
    a_map[b[0]][b[1]] = 1
    a_map[c[0]][c[1]]= 1
    while v_map:
        y,x = v_map.pop(0)
        for n_y, n_x in move:
            if n>y + n_y>=0 and m>x + n_x>=0 and a_map[y+n_y][x + n_x] == 0:
                a_map[y+n_y][x+n_x] = 2
                v_map.append((y+n_y, x+n_x))
    #print(a_map)
    for a in range(n):
        answer += a_map[a].count(0)
    ans_list.append(answer)


print(max(ans_list))






