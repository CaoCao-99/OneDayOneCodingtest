stack = []
n, k = map(int,input().split())
data = input()
stack.append(int(data[0]))
if n == k:
    print()
    exit()
for i in range(1, len(data)):
    while len(stack) + (n - i) > n-k and len(stack) > 0 and stack[len(stack) - 1] < int(data[i]):
        stack.pop()
    stack.append(int(data[i]))
#print(stack)
#stack = []
for i in range(n-k):
    print(stack[i], end= '')