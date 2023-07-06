f,s,g,u,d = map(int,input().split())


stairs = [1000001] * 1000001
q = [s]
stairs[s] = 0

while q:
    my_place = q.pop(0)
    for i in [u,-d]:
        if 1 <= my_place + i <=f:
            if stairs[my_place +i] > stairs[my_place]+1:
                stairs[my_place +i] = stairs[my_place]+1
                q.append(my_place+i)

if stairs[g] != 1000001:
    print(stairs[g])
else:
    print("use the stairs")