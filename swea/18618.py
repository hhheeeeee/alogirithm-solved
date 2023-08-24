def find(p):
    while p!= root[p]:
        p = root[p]
    return root[p]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        root[b] = a
    else:
        root[a] = b


N = int(input())
arr = list(map(int, input().split()))
root = [i for i in range(N)]

for _ in range(int(input())):
    s, a, b = input().split()
    if s == 'alliance':
        union(ord(a) - 65, ord(b) - 65)
    else:
        powera, powerb = 0, 0
        aa = []
        bb = []
        for i in range(N):
            if root[i] == root[ord(a) - 65]:
                powera += arr[i]
                aa.append(i)
            if root[i] == root[ord(b) - 65]:
                powerb += arr[i]
                bb.append(i)
        if powera > powerb:
            for i in bb:
                arr[i] = 0
        elif powera < powerb:
            for i in aa:
                arr[i] = 0
        else:
            for i in bb:
                arr[i] = 0
            for i in aa:
                arr[i] = 0

# 0보다 큰 원소의 개수 찾기
res = len([x for x in arr if x != 0])
print(res)