import sys

sys.stdin = open('3.txt')
input = sys.stdin.readline
from collections import deque


# 0은 길, 1은 벽
# 출발점부터 도착지점까지 갈 수 있는 길이 있는지 판단해라
# 가능하면 1 가능하지 않다면 0 출력

def BFS(sx, sy):
    res = 0
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 16 and 0 <= ny < 16:
                if arr[nx][ny] == -3:
                    res = 1
                    return res
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))
    return res


for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().strip())) for _ in range(16)]
    flag1, flag2 = 0, 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                sx, sy = i, j
                flag1 = 1
            if arr[i][j] == 3:
                arr[i][j] = -3
                ex, ey = i, j
                flag2 = 1
        if flag1 and flag2:
            break
    print(f'#{tc} {BFS(sx, sy)}')