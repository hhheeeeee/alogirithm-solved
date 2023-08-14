import sys
from collections import deque
sys.stdin = open('test.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    maxv = 0
    for col in range(n):
        rcnt = 0
        for row in range(m):
            if row < m - 1:
                if MAP[col][row] == 1:
                    rcnt = rcnt + 1
                else:
                    maxv = max(maxv, rcnt)
                    rcnt = 0
            else:
                maxv = max(maxv, rcnt + (MAP[col][row]))

    for row in range(m):
        ccnt = 0
        for col in range(n):
            if col < n - 1:
                if MAP[col][row] == 1:
                    ccnt = ccnt + 1
                else:
                    maxv = max(maxv, ccnt)
                    ccnt = 0
            else:
                maxv = max(maxv, ccnt + (MAP[col][row]))

    print(f'#{tc} {maxv}')
