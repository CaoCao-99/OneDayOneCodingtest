graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
data = list(map(int, input().split()))
answer = 0
def move(cnt, ans, horse):
    global answer
    if cnt == 10:
        answer = max(answer, ans)
        return
    for i in range(4):
        now = horse[i]
        if len(graph[now]) == 2:    #파란색 화살표가 있는 곳에 있는 경우(10,20,30)
            now = graph[now][1]
        else:
            now = graph[now][0]
        
        for j in range(1, data[cnt]):
            now = graph[now][0]
        if now == 32 or (now < 32 and now not in horse):
            a = horse[i]
            horse[i] = now
            move(cnt + 1, ans + score[now], horse)
            horse[i] = a

move(0,0,[0,0,0,0])
print(answer)