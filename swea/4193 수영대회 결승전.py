import sys
sys.stdin = open('1.txt')
from collections import deque

def bfs(sx, sy):
    q = deque([(sx, sy, 0)])
    while q:
        x, y, t = q.popleft()
        # if x == ex and y == ey:
        #     return t
        for dx, dy in [(1, 0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:
                if t % 3 == 2: # 소용돌이 없을 때는 1빼고 다 지나갈 수 있음
                    if not visited[nx][ny] and arr[nx][ny] != 1:
                        if not visited[nx][ny] or visited[nx][ny] > t + 1:
                            visited[nx][ny] = t + 1
                        q.append((nx, ny, t + 1))

                else: # 소용돌이 있을 때는 0만 지나갈 수 있음
                    if not visited[nx][ny] and arr[nx][ny] == 0:
                        if not visited[nx][ny] or visited[nx][ny] > t + 1:
                            visited[nx][ny] = t + 1
                        q.append((nx, ny, t + 1))
                    if arr[nx][ny] == 2: # 만약 다음 소용돌이면 기다리기
                        q.append((x, y, t+1))
    # return -1

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = -1
    bfs(sx, sy)
    print(f'#{tc} {visited[ex][ey]}')
