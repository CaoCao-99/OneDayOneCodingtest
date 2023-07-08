S = input()
n = int(input())
A = []
length = [[] for i in range(101)]  #length 배열 생성

for i in range(n):
    A.append(input())
    length[len(A[i])].append(A[i])

dp = [0] * (len(S)+1)
dp[0] = 1
end = 1

for i in range(len(S)):
    if dp[i] == 1:
        for j in range(1,len(S)+1):
            #print(j)
            if length[j] != None:
                for x in length[j]:
                    end = j
                    if S[i :i + end] == x:
                        dp[i + end] = 1
                        break
print(dp[len(S)])

