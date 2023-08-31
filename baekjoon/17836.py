import sys
sys.stdin = open('1.txt')

from collections import deque

def bfs(x, y):
    global rres

    q = deque([(x, y)])
    visited = [[float('inf')] * M for _ in range(N)]
    visited[0][0] = 0
    kx, ky = 0, 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != 1:
                    if arr[nx][ny] == 2:
                        kx, ky = nx, ny
                    if visited[x][y] + 1 < visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

    if kx != 0 or ky != 0:
        rres = visited[kx][ky] + N - kx + M - ky - 2

    if visited[N - 1][M - 1] != float('inf'):
        rres = min(rres, visited[N - 1][M - 1])



N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
rres = float('inf')

bfs(0, 0)


if rres <= T:
    print(rres)
else:
    print('Fail')

'''
4 4 10
0 0 0 1
1 1 0 1
2 0 0 1
1 1 1 0
=10

5 4 100
0 1 2 1
0 1 0 1
0 0 0 0
1 1 1 1
0 0 0 0
=11

1 4 10
0 2 1 0
=3

5 5 100
0 0 0 0 0
0 1 1 1 0
0 1 2 0 0
0 1 1 0 0
0 0 1 0 0
=8

4 4 9
0 1 0 2
0 1 0 0
0 0 0 1
0 1 1 0
=Fail

3 11 20
0 1 2 1 1 1 1 1 1 1 1
0 0 0 1 0 0 0 1 1 1 1
0 1 0 0 0 1 0 0 0 0 0
=14

5 11 25
0 1 2 0 0 1 1 1 1 1 1
0 1 1 1 0 0 0 1 1 1 1
0 0 0 0 0 1 0 1 0 0 0
0 1 1 1 1 1 0 1 0 1 0
0 1 1 1 1 0 0 0 0 1 0
=20

4 4 100
0 1 1 1
0 1 2 0
0 0 0 0
1 1 1 1
=8

7 7 100
0 0 0 0 0 0 0
0 1 1 1 1 1 2
0 0 0 0 0 0 0
1 1 1 0 1 1 1
0 0 0 0 0 0 1
0 1 1 1 1 1 1
0 0 0 0 0 0 0
=12

4 10 100
0 1 1 1 1 2 1 1 1 1
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
=14

4 4 10
0 0 0 0
0 0 1 0
0 1 2 1
0 0 0 0
=6
'''