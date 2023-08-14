N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * (N+1)
result = []

def dfs(start, depth):
   prev = 0
   if depth == M:
        print(*result)
        return

   for i in range(start,N):
        if arr[i] != prev and not visited[i]:
            visited[i] = True
            prev = arr[i]
            result.append(arr[i])
            dfs(i+1, depth+1)
            result.pop()
            visited[i] = False

dfs(0,0)