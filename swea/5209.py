def check(depth, nsum):
    global minv
    if nsum > minv: return

    if depth == N:
        minv = min(minv, nsum)
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            check(depth + 1, nsum + arr[depth][i])
            visited[i] = False




for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minv = float('inf')
    visited = [False] * (N + 1)
    check(0, 0)
    print(f'#{tc} {minv}')