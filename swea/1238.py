import sys

sys.stdin = open('3.txt')
input = sys.stdin.readline
from collections import deque

def BFS(S):
    maxcnt, maxnum = 0, 0
    q = deque([(S, 0)])
    visited[S] = True
    while q:
        now, cnt = q.popleft()
        if cnt > maxcnt:
            maxcnt = cnt
            maxnum = now

        if cnt == maxcnt:
            if now > maxnum:
                maxnum = now

        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append((next, cnt+1))

    return maxnum

for tc in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    visited = [False] * 101
    for i in range(0, N-1, 2):
        if arr[i+1] not in graph[arr[i]]:
            graph[arr[i]].append(arr[i+1])

    print(f'#{tc} {BFS(S)}')
