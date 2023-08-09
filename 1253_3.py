N = int(input())
data = list(map(int, input().split()))
data = sorted(data)
answer = 0

for i in range(N):
    new_data = data[:i] + data[i+1:]
    left, right = 0, len(new_data) - 1
    while left < right:
        tmp = new_data[left] + new_data[right]
        if tmp == data[i]:
            answer += 1
            break
        if tmp < data[i]:
            left += 1
        else:
            right -= 1
print(answer)
