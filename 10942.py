n = int(input())
data = list(map(int,input().split()))
m = int(input())
slicing_data = []
for i in range(m):
    a,b = map(int,input().split())
    slicing_data.append((a,b))

for a,b in slicing_data:
    if a == b:
        print(1)
    elif (b-a)%2 == 0:
        if data[a-1:(a+b)//2-1] == data[(a+b)//2+1:b][::-1]:
            print(1)
        else:
            print(0)
    else:
        if data[a-1:(a+b)//2+1] == data[(a+b)//2+1:b][::-1]:
            print(1)
        else:
            print(0)