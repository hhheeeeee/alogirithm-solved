import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def compare(i, j, b):
    paint = 0
    for x in range(8):
        for y in range(8):
            if board[i+x][j+y] != b[x][y]:
                paint += 1
    return paint

b1 = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
b2 = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']

N ,M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

minv = 300
for i in range(N-7):
    for j in range(M-7):
        minvv = min(compare(i, j, b1), compare(i, j, b2))
        minv = min(minv, minvv)
print(minv)