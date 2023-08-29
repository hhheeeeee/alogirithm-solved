from collections import deque

def BFS(S):
    q = deque([S])
    visited[S] = True
    while q:
        now = q.popleft()
        print(now)
        for idx, next in enumerate(graph[now]):
            if next == 1 and not visited[idx]:
                visited[idx] = True
                q.append(idx)
    return 0

S = int(input())
visited = [False] * 6
graph = [[0,0,0,0,1,0],
         [1,0,1,0,0,1],
         [1,0,0,1,0,0],
         [1,1,0,0,0,0],
         [0,1,0,1,0,1],
         [0,0,1,1,0,0]
]
BFS(S)