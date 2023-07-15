num = int(input())
answer = []
for i in range(num):
    data = dict()
    string_data = input()
    k = int(input())
    for let in range(len(string_data)):
        if not string_data[let] in data:
            data[string_data[let]] = [let]
        else:
            data[string_data[let]].append(let)
    ans_a = 99999999
    ans_b = -1
    for j in data.keys():
        if len(data[j]) >= k:
            seq = data[j]
            for start in range(len(data[j]) - k + 1):
                ans_a = min(ans_a, data[j][k + start -1] - data[j][start] + 1)
                ans_b = max(ans_b, data[j][k + start -1] - data[j][start] + 1)
    if ans_b == -1:
        answer.append([-1])
    else:
        answer.append([ans_a, ans_b])
    #print(data)

for i in range(num):
    for j in answer[i]:
        print(j, end=' ')
    print()
