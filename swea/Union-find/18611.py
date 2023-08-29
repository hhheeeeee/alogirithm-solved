def find(node):
    if node != root[node]:
        root[node] = find(root[node])
    return root[node]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    if rank[root_x] > rank[root_y]:
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1


N = int(input())
rank = [0] * 26
root = [i for i in range(26)]
for _ in range(N):
    a, b = input().split()
    union(ord(a) - 65, ord(b) - 65)

for i in range(26):
    find(i)

DAT = [0] * 26

for i in range(26):
    DAT[root[i]] += 1  # 각 루트별 노드 개수 세기

team = 0
indi = 0
for data in DAT:
    if data > 1:
        team += 1
    elif data == 1:
        indi += 1

print(team)
print(indi)