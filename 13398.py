n = int(input())
data = list(map(int,input().split()))
real_answer = []
answer = -9999999999999

def check(start):
    new_start = data[start]
    max_num = 0
    max_num = max(max_num, new_start)
    for i in range(start+1, n):
        new_start+=data[i]
        max_num = max(max_num, new_start)
    return max_num



for i in range(n):
    next = data[i]
    answer += data[i]
    if answer <= next:
        answer = next
    elif next < 0 and i+1 < n:
        real_answer.append(answer-next + check(i+1))
    real_answer.append(answer)

print(max(real_answer))