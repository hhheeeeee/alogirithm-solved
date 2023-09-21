def dfs(depth, prob):
    global maxv
    if depth == N:
        maxv = max(maxv, prob)
        return

    if prob * (100 ** (N - depth)) < maxv:
        return
    
    for i in range(N):
        if arr[depth][i] == 0:
            continue
        if not visited[i]:
            visited[i] = True
            prob *= arr[depth][i]
            dfs(depth + 1, prob)
            visited[i] = False
            if arr[depth][i]:
                prob /= arr[depth][i]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split() )) for _ in range(N)]
    visited = [False] * N
    maxv = 0
    dfs(0, 1)
    print(f'#{tc} {maxv / (100 ** (N- 1)):.6f}')
