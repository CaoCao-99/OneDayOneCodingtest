l_s = []
r_s = []
left = []
c_l = []
c_r = []
right = []
n = int(input())
data = list(map(int,input().split()))


for i in range(n):
    if l_s:
        if l_s[-1][0] > data[i]:
            l_s.append([data[i], i])
        else:
            while l_s and l_s[-1][0] <= data[i]:
                l_s.pop()
            l_s.append([data[i], i])
    else:
        l_s.append([data[i],i])
    left.append(len(l_s) - 1)
    if len(l_s) >= 2:
        c_l.append(l_s[-2][1])
    else:
        c_l.append(99999999)


for i in range(n-1,-1,-1):

    if r_s:
        if r_s[-1][0] > data[i]:
            r_s.append([data[i], i])
        else:
            while r_s and r_s[-1][0] <= data[i]:
                r_s.pop()
            r_s.append([data[i], i])
    else:
        r_s.append([data[i],i])

    right.append(len(r_s) - 1)
    if len(r_s) >= 2:
        c_r.append(r_s[-2][1])
    else:
        c_r.append(99999999)


for i in range(n):
    if c_l[i] == c_r[n-1-i] == 99999999:
        print(left[i] + right[n-1-i])
    else:
        a = abs(i - c_l[i])
        b = abs(i - c_r[n-1-i])
        if a == b:
            print(left[i] + right[n-1-i], min(c_l[i], c_r[n-1-i])+1)
        elif a > b:
            print(left[i] + right[n-1-i], c_r[n-1-i] + 1)
        else:
            print(left[i] + right[n-1-i], c_l[i]+1)






