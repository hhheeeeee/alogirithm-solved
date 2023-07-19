import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline
from collections import deque

def is_valid(q, board):
    # q에서 하나씩 뽑아서 가로 세로 확인
    # 하나라도 안되면 no
    while q:
        x, y = q.popleft()
        rcnt, ccnt = 0, 0
        # 가로, 세로 체크
        for i in range(8):
            if board[x][i] == 'O':
                rcnt += 1
            if board[i][y] == 'O':
                ccnt += 1
        if rcnt != 1 or ccnt != 1:
            return 'no'

    return 'yes'

T = int(input())
for testcase in range(1, T+1):
    board = [input().strip() for _ in range(8)]
    q = deque([])
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'O':
                q.append((i,j))
    if len(q) == 8:
        answer = is_valid(q, board)
    else:
        answer = 'no'
    print(f"#{testcase} {answer}")