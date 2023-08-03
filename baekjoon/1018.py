import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def paint(i, j, color):
    p1, p2 = 0, 0
    for c in range(8):
        for r in range(8):
            if (c + r) % 2 == 0:
                p1 += (board[i + c][j + r] != color)
                p2 += (board[i + c][j + r] == color)
            else:
                p1 += (board[i + c][j + r] == color)
                p2 += (board[i + c][j + r] != color)
    return min(p1, p2)

N ,M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
minv = 300
for i in range(N-7):
    for j in range(M-7):
        minv = min(minv,paint(i, j, board[i][j]))
print(minv)