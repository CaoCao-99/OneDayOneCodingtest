n, k = map(int,input().split())
cnt = 0
data = [2 ** i for i in range(0, 27)]
answer = 99999999999999


for i in range(1,k+1):
    orig = n
    for c in range(i):
        for j in range(len(data)-1):
            if data[j] <= orig < data[j+1]:
                orig -= data[j]
                answer = min(answer, data[j] - orig)
                break
    if orig == 0:
        print(0)
        exit()



print(answer)

