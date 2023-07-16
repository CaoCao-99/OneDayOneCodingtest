def get_count(i, cnt):
    if i // 2 > 0:
        cnt = get_count(i//2, cnt+1)
    return cnt

start, end = map(int,input().split())
s_c, e_c = get_count(start, 0), get_count(end,0)
# 0 , 1 10, 11, 100, 101, 110, 111
count_s = 0
count_e = 0

sum_b = [0 for _ in range(51)]

for i in range(1, 51):
    sum_b[i] += 2**(i-1) + sum_b[i-1]
    print(sum_b[i])
#1,3,7,


print(sum_b)


