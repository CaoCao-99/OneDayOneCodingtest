import copy
n = int(input())
start = input()
start = [int(i) for i in start]
want = input()
want = [int(i) for i in want]
print(want)
answer = 1000000000000000
child = [[0,0,0] ]
def change(cnt, ans, now):
    global answer
    if cnt > answer:
        return 9999999999999999
    if ans == want:
        answer = min(answer, cnt)
        if cnt == answer:
            return answer
        else:
            return 9999999999999999
    if now == len(want) - 1:
        return cnt
    if want[now] == ans[now]:
        change(cnt, ans, now + 1)

    elif want[now] > ans[now]:
        data = copy.deepcopy(ans)
        for i in range(now, len(data)):
            data[i] = (data[i] + want[now] - ans[now])%10
        d1 = change(cnt + want[now] - ans[now], data, now + 1)
        data = copy.deepcopy(ans)
        data[now] = want[now]
        chai = (10 + ans[now] - want[now])%10
        d2 = change(cnt + chai, data, now + 1)
        if d1 < d2 :
            print(now + 1, - want[now] + ans[now])
        else:
            print(now + 1, chai)

    else:
        chai = ans[now] - want[now]
        data = copy.deepcopy(ans)
        data[now] = want[now]
        d1 = change(cnt + chai, data, now + 1)
        data = copy.deepcopy(ans)
        chai2 = (10 - int(ans[now]) + want[now])%10
        for i in range(now, len(data)):
            data[i] = (data[i] + chai2)%10
        d2 = change(cnt + chai2, data, now + 1)
        if d1 < d2 :
            print(now + 1,  - chai)
        else:
            print(now + 1, chai2)
    return cnt

change(0, start, 0)
print(answer)