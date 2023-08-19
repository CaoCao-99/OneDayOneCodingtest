n, m = map(int,input().split())
redge = [list(map(int,input().split())) for _ in range(m+1)]



def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])

def UnionParent(parent, a,b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solve(rev):
    cnt = 0
    parent = [i for i in range(n+1)]
    edge = sorted(redge, key = lambda  x : x[2], reverse=rev)
    for i in range(m+1):
        if getParent(parent, edge[i][0]) != getParent(parent, edge[i][1]):
            if edge[i][2] == 0:
                cnt +=1
            UnionParent(parent, getParent(parent,edge[i][0]), getParent(parent,edge[i][1]))
    return cnt ** 2

print(- solve(True) + solve(False))            

