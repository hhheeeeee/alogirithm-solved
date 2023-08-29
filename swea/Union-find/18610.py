from collections import deque

def bfs(start, end):
    visited = [False] * (N + 1)
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        if now == end:
            return True
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
    return False

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(Q):
    key, a, b = map(int, input().split())
    if key:
        graph[a].append(b)
        graph[b].append(a)
    else:
        if bfs(a, b):
            print('YES')
        else:
            print('NO')