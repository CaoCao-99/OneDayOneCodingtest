import copy 
data = list(map(int,input().split()))

n = len(data) - 1

dp= [[0 for j in range(2)] for i in range(n)]
foot = [[[0,0] for j in range(2)] for i in range(n)]
dp[0][0], dp[0][1] = 2,2
foot[0][0] = [data[0],0]
foot[0][1] = [0,data[0]]
#foot[i][0] = i번째에 왼발을 움직인 경우의 발 상황
#foot[i][1] = i번쨰에 오른발을 움직인 경우의 발 상황

for i in range(1, n):
    #왼발
    #만약 왼발로 옮기려고 했는데 이전에 오른발을 쓴 경우에 오른발의 위치와 같으면 불가, 이전에 왼발을 쓴 경우에 경우에 오른발의 위치와 같아도 불가
    ll = 0
    rl = 0
    if foot[i-1][0][1] == data[i]:
        l,r = foot[i-1][1]
        if l == 0 :
            dp[i][0] = dp[i-1][1] + 2
        if l == data[i]:
            dp[i][0] = dp[i-1][1] + 1

        elif abs(l-data[i]) % 2 ==0:
            dp[i][0] = dp[i-1][1] + 4
        else:
            dp[i][0] = dp[i-1][1] + 3

        foot[i][0] = [data[i],r]

    elif foot[i-1][1][1] == data[i]:
        l,r = foot[i-1][0]
        if l == 0:
            dp[i][0] = dp[i-1][0] + 2
        if l == data[i]:
            dp[i][0] = dp[i-1][0] + 1

        elif abs(l-data[i]) % 2 ==0:
            dp[i][0] = dp[i-1][0] + 4
        else:
            dp[i][0] = dp[i-1][0] + 3

        foot[i][0] = [data[i],r]

    else:
        b = foot[i-1][0][0]
        c = foot[i-1][1][0]
        if b == 0:
            ll = 2
        elif data[i] == b:
            ll = 1
        elif abs(data[i] - b)%2 ==0:
            ll = 3
        else:
            ll = 4
        if c == 0:
            rl = 2
        elif data[i] == c:
            rl = 1
        elif abs(data[i] - c)%2 == 0:
            rl = 3
        else:
            rl=4 

        dp[i][0] = min(dp[i-1][0] + ll , dp[i-1][1] + rl)
        if dp[i][0] == dp[i-1][0] + ll:
            foot[i][0] = [data[i], foot[i-1][0][1]]
        else:
            foot[i][0] = [data[i],foot[i-1][1][1]]
            

    #오른발
    #왼발
    #만약 오른발로 옮기려고 했는데 이전에 오른발을 쓴 경우에 왼발의 위치와 같으면 불가, 이전에 왼발을 쓴 경우에 경우에 왼발 위치와 같아도 불가
    ll = 0
    rl = 0
    #이전에 왼발을 쓴 경우에
    if foot[i-1][0][0] == data[i]:
        l,r = foot[i-1][1]
        if r == 0 :
            dp[i][0] = dp[i-1][1] + 2

        if r == data[i]:
            dp[i][0] = dp[i-1][1] + 1

        elif abs(r-data[i]) % 2 ==0:
            dp[i][0] = dp[i-1][1] + 4
        else:
            dp[i][0] = dp[i-1][1] + 3

        foot[i][1] = [l,data[i]]

    elif foot[i-1][1][1] == data[i]:
        l,r = foot[i-1][0]
        if r == 0:
            dp[i][0] = dp[i-1][0] + 2

        if r == data[i]:
            dp[i][0] = dp[i-1][0] + 1

        elif abs(r-data[i]) % 2 ==0:
            dp[i][0] = dp[i-1][0] + 4
        else:
            dp[i][0] = dp[i-1][0] + 3

        foot[i][1] = [l,data[i]]

    else:
        b = foot[i-1][0][1]
        c = foot[i-1][1][1]
        if b == 0:
            ll = 2
        if data[i] == b:
            ll = 1
        elif abs(data[i] - b)%2 ==0:
            ll = 3
        else:
            ll = 4
        if c == 0:
            rl = 2
        if data[i] == c:
            rl = 1
        elif abs(data[i] - c)%2 == 0:
            rl = 3
        else:
            rl=4 

        dp[i][1] = min(dp[i-1][0] + ll , dp[i-1][1] + rl)
        if dp[i][1] == dp[i-1][0] + ll:
            foot[i][1] = [foot[i-1][0][1], data[i]]
        else:
            foot[i][1] = [foot[i-1][1][1],data[i]]

    print(foot[i][0])
    print(foot[i][1])
print(min(dp[n-1]))