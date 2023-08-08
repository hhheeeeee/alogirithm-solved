import sys
sys.stdin = open('3.txt')
input = sys.stdin.readline

def is_p(board, N, M):
    for i in range(N):
        for j in range(N-M+1):
            # 가로
            h = board[i][j:j+M]
            # 세로
            v = [board[k][i] for k in range(j, j+M)]

            if h == h[::-1]:
                return h
            if v == v[::-1]:
                return v


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    result = is_p(board, N, M)
    print(f'#{tc} {"".join(result)}')



