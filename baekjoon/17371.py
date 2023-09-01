from collections import deque

def pick(depth, NN, start):
    if depth == NN:
        a = temp[:]
        pp.append(a)
        return

    for i in range(start, N + 1):
        temp.append(i)
        pick(depth + 1, NN, i + 1)
        temp.pop()

def valid(group):
    visited = [False] * (N + 1)
    # 내가 지금 속한 그룹 안에서만 타고 타고 가서 나를 다시 만난다면
    q = deque([(group[0])])
    visited[group[0]] = True
    while q:
        now = q.popleft()
        for next in adj[now]:
            if next in group:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
    for i in group:
        if not visited[i]:
            return False
    return True


N = int(input())
po = list(map(int, input().split()))
adj = [set() for _ in range(N + 1)]

for i in range(1 ,N + 1):
    line = list(map(int, input().split()))
    for a in line[1:]:
        adj[i].add(a)
        adj[a].add(i)
# 두 구역으로 나누기
# N을 2 그룹으로 나누기 => 두 그룹이 모두 유혀한지 확인하기 => 인구수 계산하기
minv = float('inf')
total = [i for i in range(1, N + 1)]
for i in range(1, N // 2 + 1): #만약에 N = 5이면 (1, 4), (2, 3) 까지만 확인하면 됨
    pp = []
    temp = []
    pick(0, i, 1)
    # pp에 i개 만큼 뽑을 수 있는 경우가 담겨 잇음 ex) 1, 2, 3, 4 => 12 13 14 23 24 34
    for one in pp:
        two = [i for i in total if i not in one]
        if valid(one) and valid(two):
            pone = [po[i - 1] for i in one]
            ptwo = [po[i - 1] for i in two]
            minv = min(minv, abs(sum(pone) - sum(ptwo)))
if minv < float('inf'):
    print(minv)
else:
    print(-1)