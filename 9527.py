def get_count(i, cnt):
    if i // 2 > 0:
        cnt = get_count(i//2, cnt+1)
    return cnt

def rec(i, sum_b):
    if sum_b[i] != 0:
        return sum_b[i]
    sum_b[i] += 2**(i-1) + rec(i-1, sum_b)
    return sum_b[i]


start, end = map(int,input().split())
s_c, e_c = get_count(start - 1, 0), get_count(end,0)

# 0 , 1 [10, 11], [100, 101, 110, 111] [1000 1001 1010 1]
# 1, 3, 8
count_s = 0
count_e = 0

sum_b = [0 for _ in range(51)]
sum_b[1]=1
#rec(50, sum_b)

#재귀문 써야 할 듯
for i in range(1, 51):
    sum_b[i] = 2**(i-1) + sum(sum_b[:i])

#숫자의 그룹을 알아내는 것이 중요하다. 그룹 내에서 몇번째인지도 중요하다


print(sum_b)

print(s_c, start - 2 ** s_c, e_c, end - 2 ** e_c)
ans_s = 0
for i in range(s_c + 1):
    ans_s += sum_b[i]

ans_e = 0






print(ans_e - ans_s)  







