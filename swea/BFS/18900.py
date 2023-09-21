from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

coco = int(input())

visited = [0] * (N+1)
visited[coco] = 1
queue = deque([coco])
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            queue.append(i)

print(max(visited.count(1) - 1, 0))