import copy
size = int(input())
a,b = map(int,input().split())
data_a = [int(input()) for _ in range(a)]
data_b = [int(input()) for _ in range(b)]
for i in range(1,a):
    data_a[i] += data_a[i-1]
for i in range(1,b):
    data_b[i] += data_b[i-1]
pizza_a = dict()
pizza_b = dict()


#0,1

    



for i in range(a):
    if not data_a[i] in pizza_a:
        pizza_a[data_a[i]] = 1
    else:
        pizza_a[data_a[i]] += 1
for i in range(b):
    if not data_b[i] in pizza_b:
        pizza_b[data_b[i]] = 1
    else:
        pizza_b[data_b[i]] += 1

#0~a-1, 1~a-1, 2~1, 3~2, 4~3, 5~4
#data[a-1], data[1~a-1] - data[0], {data[2~a-1], (data[a-1] + data[0])} - data[1] + , {data[3~a-1]} 
#2일때, data[2]-data[1],data[3] - data[1],..,data[a-1]-data[1],
# start:2 end:(3,4,5,6,..,a-1,0) -> data[2] - data[1], data[a-1]-data[1], data[a-1]-data[1]+data_a[0]
# start:3 end:(4,5,6,..,a-1,0,1) -> data[3] - data[2], data[a-1]-data[2], data[a-1]-data[2]+data_a[0], data[a-1]-data[2]+data_a[1]
# start:4 end:(4,5,6,..,a-1,0,1) -> data[4] - data[3], data[a-1]-data[2], data[a-1]-data[2]+data_a[0], data[a-1]-data[2]+data_a[1]
# start:a-2 end:(a-1,0,1,2,3,4,5..,a-3) - > data[a-1] - data[a-2], data[a-1] - data[a-2] + data[0], data[a-1] - data[a-2] + data[1], .., data[a-1] - data[a-2] + data[a-3]


for i in range(a-1):#
    for j in range(1,a):
        if i+j >= a:
            kab = data_a[a-1] - data_a[i] + data_a[(i+j)%a]
            if not kab in pizza_a:
                pizza_a[kab] = 1
            else:
                pizza_a[kab] += 1
        else:
            kab = data_a[i+j] - data_a[i]
            if not kab in pizza_a:
                pizza_a[kab] = 1
            else:
                pizza_a[kab] += 1

for i in range(b-1):#
    for j in range(1,b):
        if i+j >= b:
            kab = data_b[b-1] - data_b[i] + data_b[(i+j)%b]
            if not kab in pizza_b:
                pizza_b[kab] = 1
            else:
                pizza_b[kab] += 1
        else:
            kab = data_b[i+j] - data_b[i]
            if not kab in pizza_b:
                pizza_b[kab] = 1
            else:
                pizza_b[kab] += 1


answer = 0
pizza_a[0] = 1
pizza_b[0] = 1
for i in range(size+1):
    if i in pizza_a and size-i in pizza_b:
        answer += pizza_a[i] * pizza_b[size-i]
# print(pizza_b)
# print(pizza_a)
print(answer)