import itertools
A_goal = int(input())/100
B_goal = int(input())/100
n_prime = {0,1,4,6,8,9,10,12,14,15,16,18}
A = [0] * 19
B = [0] * 19


for i in range(19):
    A[i] = A_goal**i * (1-A_goal)**(18-i) * len(list(itertools.combinations(range(18),i)))
    B[i] = B_goal**i * (1-B_goal)**(18-i) * len(list(itertools.combinations(range(18),i)))
    
mix = 0
mix_a = 0
mix_b = 0
for i in n_prime:
    for j in n_prime:
        mix += A[i] * B[j]


print(1-mix)