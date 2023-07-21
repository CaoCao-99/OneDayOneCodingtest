n, k = map(int,input().split())
data = list(map(int,input().split()))
new_data = [0 for i in range(n-1)]

for i in range(n-1):
    new_data[i] = data[i+1] - data[i]

a = sorted(new_data)
print(a)
print(sum(a[:n-k]))

