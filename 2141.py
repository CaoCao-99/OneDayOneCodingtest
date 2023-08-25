n = int(input())
data = [list(map(int,input().split())) for i in range(1,n+1)]
for i in range(1,n+1):
    data[i-1].append(i)
data = sorted(data)
people = sum([subdata[1] for subdata in data])//2
cnt = 0
for a,b,c in data:
    cnt += b
    if cnt >= people:
        print(c)
        exit()

    