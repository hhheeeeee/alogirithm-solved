from collections import deque
def bfs(coco):
    q = deque([coco])
    visited[coco] = True
    while q:
        new = q.popleft()
        for next in graph[new]:
            if not visited[next]:
                visited[next] = True
                q.append(next)


N = int(input())
T = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(T):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
coco = int(input())
goal = int(input())
bfs(coco)
if not visited[goal]:
    print('NO')
else:
    print('YES')