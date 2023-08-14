N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

def dfs(start, depth):
    if depth == M:
        print(*result)
        return

    prev = 0
    for i in range(start, N):
        if arr[i] == prev:
            continue
        prev = arr[i]
        result.append(arr[i])
        dfs(i, depth+1)
        result.pop()

dfs(0, 0)