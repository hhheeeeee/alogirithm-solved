import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline
from collections import deque

n, m, h = map(int, input().split())
box = []
for _ in range(h):
    box.append([list(map(int, input().split())) for _ in range(m)])

# 익은 토마토 위치 찾기
tomato = deque([])
for z in range(h):
    for y in range(m):
        for x in range(n):
            if box[z][y][x] == 1:
                tomato.append((z, y, x))

dir = [(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(1,0,0),(-1,0,0)]

def bfs():
    # 토마토 익어가기
    while tomato:
        z, y, x = tomato.popleft()
        for dz, dy, dx in dir:
            nz, ny, nx = z+dz, y+dy, x+dx
            if 0<=nz<h and 0<=ny<m and 0<=nx<n:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    tomato.append((nz, ny, nx))
    
    # 토마토 다 익은 다음에 확인
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if box[z][y][x] == 0:
                    return -1
    maxv = 0
    for i in range(h):
        maxv = max(max(map(max, box[i])),maxv)
    return maxv - 1

print(bfs())
