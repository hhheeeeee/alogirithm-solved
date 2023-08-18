import sys
sys.stdin = open('1.txt')
from collections import deque
INF = 10e7

def BFS():
    q = deque([(0,0)])
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0),(0,1),(-1,0),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:
                # 지금 내가 가려고 하는데 비용이 더 적으면 적은 비용으로 갱신
                if visited[x][y] + arr[nx][ny] < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    q.append((nx, ny))
    return visited

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[INF] * N for _ in range(N)]
    BFS()
    print(f'#{tc} {visited[N-1][N-1]}')
