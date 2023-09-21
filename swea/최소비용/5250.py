import sys
sys.stdin = open('1.txt')
from collections import deque
INF = float('inf')

def bfs():
    q = deque([(0,0)])
    visited[0][0] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:
                # 지금까지 든 비용 + arr 비용 + (높이) < visited 이면 갱신
                if arr[nx][ny] > arr[x][y]:
                    cost =  visited[x][y] + (arr[nx][ny] - arr[x][y]) + 1
                else:
                    cost =  visited[x][y] + 1
                if visited[nx][ny] > cost:
                    visited[nx][ny] = cost
                    q.append((nx, ny))
    
    return visited[N-1][N-1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[INF] * N for _ in range(N)]
    res = bfs()
    print(f'#{tc} {res}')
    # for i in visited:
    #     print(i)