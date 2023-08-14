n = int(input())
start = int(input())
want = int(input())
answer = 0

def change(cnt, ans, now):
    global answer
    if cnt > answer:
        return
    if ans == str(want) or now == len(str(want)) - 1:
        answer = min(answer, cnt)
        return
    plus = (want[cnt] - int(ans[cnt]))%10
    change(cnt + 1, )

    