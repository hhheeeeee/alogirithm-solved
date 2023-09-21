def find(x):
    while x != root[x]:
        x = root[x]
    return root[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        root[b] = a
    else:
        root[a] = b

def calcul(i):
    global cost
    if i == 0:
        return
    
    a = p[i]
    # a[0]은 내 부모, a[1]은 cost
    cost += a[1]
    calcul(a[0])




N, M, K = map(int, input().split())
p = [0 for i in range(N)]
root = [i for i in range(N)]
for _ in range(M):
    parent, child, cost = map(int, input().split())
    p[child] = (parent, cost)
    union(child, parent)

res = []
for i in range(1, N):
    if root[i] == 0:
        cost = 0
        calcul(i)
        if cost <= K:
            res.append(i) 

print(*res)