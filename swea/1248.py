import sys
sys.stdin = open('1.txt')

def dfs(now):
    global cnt

    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            cnt += 1
            dfs(next)

for tc in range(1, int(input())+1):
    V, E, A, B = map(int, input().split())
    root = [i for i in range(V + 1)]
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    for i in range(E):
        root[arr[i*2 + 1]] = arr[i*2]
        graph[arr[i*2]].append(arr[i*2 + 1])

    A_parents = []
    B_parents = []
    while A != root[A]:
        A_parents.append(root[A])
        A = root[A]
    while B != root[B]:
        B_parents.append(root[B])
        B = root[B]
    common_parents = 0
    for i in A_parents:
        for j in B_parents:
            if i == j:
                common_parents = i
                break
        if common_parents:
            break
    cnt = 1
    visited[common_parents] = True
    dfs(common_parents)
    print(f'#{tc} {common_parents} {cnt}')