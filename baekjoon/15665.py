N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * (N+1)
result = []

def dfs(depth):
    if depth == M:
        print(*result)
        return
    prev = 0
    for i in range(N):
        if arr[i] == prev:
            continue
        result.append(arr[i])
        prev = arr[i]
        dfs(depth + 1)
        result.pop()
dfs(0)