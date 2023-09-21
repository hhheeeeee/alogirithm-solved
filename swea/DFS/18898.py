def dfs(now, e, path):
    global res
    if now == e:
        res = sum(path) - max(path)
        return
    
    for next in adj[now]:
        if not visited[next[0]]:
            visited[next[0]] = True
            path.append(next[1])
            dfs(next[0], e, path)
            visited[next[0]] = False
            path.pop()



N, s, e = map(int, input().split())
adj = [[] for _ in range(N+1)]
res = 0
for _ in range(N-1):
    room1, room2, cost = map(int, input().split())
    adj[room1].append((room2, cost))
    adj[room2].append((room1, cost))

visited = [False] * (N+1)
visited[s] = True
dfs(s, e, [])
print(res)