
n = int(input())
data = list(map(int,input().split()))
answer = [0] * (n+1)
l_1 = [data[0]]
l_2 = [data[0]]
r_1 = [data[n-1]]
r_2 = [data[n-1]]
for i in range(1,n):
    #l_1
    if data[i] == l_1[-1]:
        if len(l_1) == 1 or data[i] != l_1[-2]:
            l_1.append(data[i])
    elif data[i] < l_1[-1]:
        l_1.append(data[i])
    else:
        while l_1 and l_1[-1] < data[i]:
            l_1.pop()
        l_1.append(data[i])
    #l_2
    if data[i] == l_2[-1]:
        if len(l_2) == 1 or data[i] != l_2[-2]:
            l_2.append(data[i])
    elif data[i] > l_2[-1]:
        l_2.append(data[i])
    else:
        while l_2 and l_2[-1] > data[i]:
            l_2.pop()
        l_2.append(data[i])
    left = max(len(l_1) - 1, len(l_2) - 1)
    answer[i+1] += left


for i in range(n-1,0,-1):
    #r_1

    if data[i] == r_1[-1]:
        if len(r_1) == 1 or data[i] != r_1[-2]:
            r_1.append(data[i])
    elif data[i] < r_1[-1]:
        r_1.append(data[i])
    else:
        while r_1 and r_1[-1] < data[i]:
            r_1.pop()
        r_1.append(data[i])
    
    #r_2

    if data[i] == r_2[-1]:
        if len(r_2) == 1 or data[i] != r_2[-2]:
            r_2.append(data[i])
    elif data[i] > r_1[-1]:
        r_2.append(data[i])
    else:
        while r_2 and r_2[-1] > data[i]:
            r_2.pop()
        r_2.append(data[i])
    right = max(len(r_1) - 1, len(r_2) - 1)
    answer[n-i] += right

print(answer)
print(max(answer))