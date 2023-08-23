data = input()
dp = [[0] * (len(data)) for _ in range(len(data))] #dp[중앙 인덱스][반지름]
answer = [9999999999] * (len(data) + 1)
answer[len(data)] = 0
for i in range(len(data)):
    dp[i][i] = 1
    if i + 1 <len(data) and data[i] == data[i+1]:
        dp[i][i+1] = 1
        

for l in range(3,len(data) + 1):
    for start in range(len(data) - l + 1):
        end = start + l - 1
        if dp[start+1][end-1] == 1 and data[start] == data[end]:
            dp[start][end] = 1


for end in range(len(data)):
    for start in range(end + 1):
        if dp[start][end]:
            answer[end] = min(answer[end], answer[start-1] + 1)
        else:
            answer[end] = min(answer[end], answer[end-1] + 1)
print(answer)
print(answer[len(data)-1])
    


