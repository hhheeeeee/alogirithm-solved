import sys

sys.stdin = open('../1.txt')

for tc in range(1, int(input()) + 1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxv = 0
    for i in range(N):
        for j in range(N):
            now = arr[i][j]
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                for p in range(1, P + 1):
                    nx, ny = i + (dx * p), j + (dy * p)
                    if 0 <= nx < N and 0 <= ny < N:
                        now += arr[nx][ny]
            maxv = max(maxv, now)
    print(f'#{tc} {maxv}')
