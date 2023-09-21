from collections import deque


def bfs(n, k):
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            return visited[now]
        for new in (now+1, now-1, 2*now, now-10):
            if 1 <= new <= 1000000 and not visited[new] and new != n:
                visited[new] = visited[now] + 1
                q.append(new)
    return -1

for tc in range(1, int(input()) + 1):
    s, e = map(int, input().split())
    visited = [0] * 2000000
    print(f'#{tc} {max(0, bfs(s, e))}')