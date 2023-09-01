import sys
from collections import deque

sys.stdin = open('../1.txt')

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]


def bfs(i, j):
    q = deque([(i, j)])
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return max(map(max,visited))

res = -float('inf')
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            res = max(res, bfs(i, j))
print(res - 1)

'''
3 3
LLW
WWW
WWW 
'''