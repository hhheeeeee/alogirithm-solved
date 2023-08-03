import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def move_side(col, row, dir):
    while True:
        if 0 <= row + dir < 100 and ladder[col][row + dir] == 1:
            row += dir
        else:
            break
    return col, row

def find_start(ladder):
    for i in range(100):
        if ladder[-1][i] == 2:
            col, row = 99, i
            break  # 시작점 찾으면 반복문 종료

    while col > 0:
        col -= 1
        if 0 <= row - 1 and ladder[col][row - 1] == 1:
            col, row = move_side(col, row, -1)
        elif row + 1 < 100 and ladder[col][row + 1] == 1:
            col, row = move_side(col, row, 1)

    return row

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    print(find_start(ladder))
