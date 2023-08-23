data = input()
dp = [[0] * (len(data)) for _ in range(len(data))] #dp[중앙 인덱스][반지름]
answer = [9999999999] * (len(data))
answer[len(data)-1] = 0
for i in range(len(data)):
    dp[i][i] = 1
    if i + 1 <len(data) and data[i] == data[i+1]:
        dp[i][i+1] = 1
        

for start in range(len(data)):
    for end in range(start+2,len(data)):
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
    


