from collections import deque
import sys
#sys.stdin = open('test.txt')
input = sys.stdin.readline
# 1년씩 증가시키면서 상하좌우 보고 값 변화시키기
# 값 변화시킨 그래프 가지고 bfs하면서 덩어리 세기
# 만약 덩어리가 2개 미만이라면 다시 1년 증가
# 만약 덩어리가 2개라면 년도 출력
# 덩어리 세면서 만약 덩어리가 0 이면 0 출력하고 종료


def year_pass(map):
    # 일단 빙산들 찾기
    ice = deque([])
    for i in range(N):
        for j in range(M):
            if map[i][j] != 0:
                ice.append((i, j))
    if not ice:
        return -1

    new_map = [[0] * M for _ in range(N)]

    while ice:
        x, y = ice.popleft()
        ocean = 0
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if map[nx][ny] == 0:
                    ocean += 1
        new_map[x][y] = max(map[x][y] - ocean, 0)

    return new_map


def bfs(sx, sy, visited):
    visited[sx][sy] = True
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and map[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


def find_chunk(map):
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if map[i][j] == 0:
                visited[i][j] = True
    chunk = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and map[i][j] != 0:
                bfs(i, j, visited)
                chunk += 1

    return chunk, visited


N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
year = 1
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while True:
    # 만약 빙산이 하나도 없다면
    new = year_pass(map)
    if new == -1:
        result = 0
        break

    chunk, visited = find_chunk(new)
    if chunk > 1:
        result = year
        break

    year += 1
    map = new

print(result)


# 반례
# input:
# 5 5
# 0 0 0 0 0'
# 0 1 1 1 0
# 0 1 0 1 0
# 0 1 1 1 0
# 0 0 0 0 0

# answer: 0
