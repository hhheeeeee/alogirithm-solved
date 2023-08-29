from collections import deque
def bfs(R):
    global res
    q = deque([(R, 0)])
    visited[R] = True
    while q:
        now, cnt = q.popleft()
        if cnt <= K:
            res += 1
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append((next, cnt+1))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
R, K = map(int, input().split())
res = 0
bfs(R)
print(res)