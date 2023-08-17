import sys

sys.stdin = open('3.txt')
input = sys.stdin.readline
from collections import deque


# 물론 이동하려는 방이 존재해야 하고,
# 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.
def bfs(x, y):
    q = deque([(x, y)])
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= ny < N and 0 <= nx < N:
                if arr[nx][ny] == arr[x][y] + 1:
                    cnt += 1
                    q.append((nx, ny))
                    break
    return cnt


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxv, room = 1, 1
    for i in range(N):
        for j in range(N):
            now = bfs(i,j)
            if now > maxv:
                maxv = now
                room = arr[i][j]
            elif now == maxv:
                if arr[i][j] < room:
                    room = arr[i][j]
    print(f'#{tc} {room} {maxv}')
