n = int(input())
data = []
head = [0 for i in range(n)]
for i in range(n):
    string = input()
    data.append((string,i))     #문자열, index

sorted_data = list(sorted(data))
for i in range(n-1):
    if sorted_data[i][1] == n-1:
        print("asd")
    if sorted_data[i][0] == sorted_data[i+1][0]:
        continue
    length = min(len(sorted_data[i][0]), len(sorted_data[i+1][0]))
    cnt = 0
    for j in range(length):
        if sorted_data[i][0][j] == sorted_data[i+1][0][j]:
            cnt+=1
        else:
            break
    head[sorted_data[i][1]] = max(head[sorted_data[i][1]], cnt)
    head[sorted_data[i+1][1]] = max(head[sorted_data[i+1][1]], cnt)


print(head)
for i in range(n):
    if head[i] == max(head):
        print(data[i][0])
        for j in range(i+1, n):
            if head[j] == max(head) and data[j][0][:head[i]] == data[i][0][:head[i]]:
                print(data[j][0])
                exit()


#반례!


# 출력:
# aaa
# aab
# 답:
# aaa
# aac

# 5
# abab
# abaa
# abcdab
# abcda
# abcdaa