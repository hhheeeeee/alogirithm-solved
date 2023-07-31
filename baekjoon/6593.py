import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline
from collections import deque

dir = [(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(1,0,0),(-1,0,0)]

def bfs():
    # 도착 위치에 가기
    while queue:
        z, y, x = queue.popleft()
        for dz, dy, dx in dir:
            nz, ny, nx = z+dz, y+dy, x+dx
            if (nz, ny, nx) == end:
                return f"Escaped in {visited[z][y][x] + 1} minute(s)."
            if 0<=nz<h and 0<=ny<m and 0<=nx<n:
                if building[nz][ny][nx] == '.' and visited[nz][ny][nx] == 0:
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    queue.append((nz, ny, nx))
    
    return 'Trapped!'

while True:
    h, m, n = map(int, input().split())
    if (h, m, n) == (0,0,0):
        break
    building = []
    for _ in range(h):
        building.append([list(input().strip()) for _ in range(m)])
        skip = input()
    visited = [[[0] * n for _ in range(m)] for _ in range(h)]

    # 시작 위치랑 도착 위치 구하기
    queue = deque([])
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if building[z][y][x] == 'S':
                    queue.append((z, y, x))
                if building[z][y][x] == 'E':
                    end = (z, y, x)
    print(bfs())
    