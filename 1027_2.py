
n = int(input())
data = list(map(int,input().split()))
answer = [0] * (n+1)
l_1 = [0]
l_2 = [0]
r_1 = [n-1]
r_2 = [n-1]

for i in range(1,n):
    #l_1
    if data[i] == data[l_1[-1]]:
        if len(l_1) == 1:
            l_1.append(i)
    elif data[i] < data[l_1[-1]]:
        if len(l_1) == 1:
            l_1.append(i)
        else:
            if abs( (data[l_1[-1]] - data[l_1[-2]])/(l_1[-1] - l_1[-2]) ) <  abs((data[i] - data[l_1[-1]])/(i - l_1[-1])):
                l_1.append(i)
    else:
        while l_1:
            l_1.pop()
        l_1.append(i)
    
    
    #l_2
    if data[i] == data[l_2[-1]]:
        if len(l_2) == 1:
            l_2.append(i)
    elif data[i] > data[l_2[-1]]:
        if len(l_2) == 1:
            l_2.append(i)
        else:
            if abs( abs(data[l_2[-1]] - data[l_2[-2]])/abs(l_2[-1] - l_2[-2]) ) <  abs(abs(data[i] - data[l_2[-1]])/abs(i - l_2[-1])):
                l_2.append(i)
    else:
        while l_2:
            l_2.pop()
        l_2.append(i)
    left = max(len(l_1) - 1, len(l_2) - 1)
    answer[i+1] += left#2~n


for i in range(n-2,-1,-1):
    #l_1
    if data[i] == data[r_1[-1]]:
        if len(r_1) == 1:
            r_1.append(i)
    elif data[i] < data[r_1[-1]]:
        if len(r_1) == 1:
            r_1.append(i)
        else:
            if abs( (data[r_1[-1]] - data[r_1[-2]])/(r_1[-1] - r_1[-2]) ) <  abs((data[i] - data[r_1[-1]])/(i - r_1[-1])):
                r_1.append(i)
    else:
        while r_1:
            r_1.pop()
        r_1.append(i)
    
    
    #l_2
    if data[i] == data[r_2[-1]]:
        if len(r_2) == 1:
            r_2.append(data[i])
    elif data[i] > data[r_2[-1]]:
        if len(r_2) == 1:
            r_2.append(i)
        else:
            if abs( abs(data[r_2[-1]] - data[r_2[-1]])/abs(r_2[-1] - r_2[-2]) ) <  abs(abs(data[i] - data[r_2[-1]])/abs(i - r_2[-1])):
                r_2.append(i)
    else:
        while r_2:
            r_2.pop()
        r_2.append(i)
    right = max(len(r_1) - 1, len(r_2) - 1)
    answer[i+1] += right#1~n-1

print(answer)
print(max(answer))