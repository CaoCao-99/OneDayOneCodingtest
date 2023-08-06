n, k, d = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(k)]
left = 1
right = n
mid = (left + right)//2

while left <= right:
    mid = (left + right)//2
    cnt = 0 
    check = False
    for a,b,c in data:

        if mid < a:
            continue
        if mid >= b:
            cnt += (b-a)//c+1
        else:
            cnt += (mid-a)//c + 1

        if d <= cnt:
            check = True
            break

    if not check:
        #answer = mid + 1
        left = mid + 1
    else:
        answer = mid
        right = mid - 1
print(answer)

