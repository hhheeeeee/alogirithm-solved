11724
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('test.txt')
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b =map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            dfs(next)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)

