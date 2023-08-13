n , k = map(int,input().split())
data = []
for i in range(n):
    data.append(int(input()))
answer = [0] * (k+1)
answer[0] = 1


def get_count(c):
    if c < 0:
        return 0
    if answer[c] != 0:
        return 1
    for i in data:
        answer[c] += get_count(c-i)
    
    return answer[c]
    


print(get_count(k))
print(answer)