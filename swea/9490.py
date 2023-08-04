import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    maxv = 0
    for x in range(N):
        for y in range(M):
            sumv = board[x][y]
            for dx, dy in [(1, 0), (0,1),(-1,0),(0,-1)]:
                nx, ny = x + dx, y + dy
                if 0<=nx<N and 0<=ny<M:
                    sumv += board[nx][ny]
            maxv = max(maxv, sumv)
    print(f'#{tc} {maxv}')
    