n_group = [0,1]

for i in range(2,60):
    n_group.append(2**(i-1))


def get_count(cnt, n_group):
    for i in range(59):
        if n_group[i] <= cnt < n_group[i+1]:
            return i 

def rec(i, sum_b, n_group):
    if i ==0:
        return 0 
    if i == 1 :
        return 1
    n_i = get_count(i, n_group)
    n_n = i - n_group[n_i]

    return sum_b[n_i-1] + n_n + 1 + rec(n_n+1, sum_b, n_group)


start, end = map(int,input().split())
start -= 1
s_c, e_c = get_count(start, n_group), get_count(end,n_group)

count_s = 0
count_e = 0

sum_b = [0 for _ in range(60)]
sum_b[1]=1
#rec(50, sum_b)

#재귀문 써야 할 듯
for i in range(1, 51):
    sum_b[i] = 2**(i-1) + sum(sum_b[:i])

for i in range(1, 51):
    sum_b[i] += sum_b[i-1]

print(s_c, start - n_group[s_c], e_c, end - n_group[e_c])
#print(2 ** 60)
if s_c == 0:
    ans_s =0
else:
    ans_s = sum_b[s_c-1] + start - n_group[s_c] + 1 + rec(start - n_group[s_c] + 1 , sum_b, n_group)

if e_c == 0:
    ans_e = 0
else:    
    ans_e = sum_b[e_c-1] + end - n_group[e_c] + 1 +rec(end - n_group[e_c] + 1, sum_b, n_group)



print(ans_e - ans_s)

#1000,1001,1010,1011, 1100
#3, 4, (4) -> 







