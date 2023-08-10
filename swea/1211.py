import sys
sys.stdin = open('../../test.txt')
input = sys.stdin.readline

def find_exit(x, y):
    cnt = 0
    while y < 100:
        if x + 1 < 100 and ladder[y][x + 1] == 1:
            while x + 1 < 100 and ladder[y][x + 1] == 1:
                x += 1
                cnt += 1
            y += 1
            continue
        elif 0 <= x - 1 and ladder[y][x - 1] == 1:
            while 0 <= x - 1 and ladder[y][x - 1] == 1:
                x -= 1
                cnt += 1
            y += 1
            continue
        y += 1
    return cnt


for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    mcnt = 10000000
    for i in range(100):
        if ladder[0][i] == 1:
            cnt = find_exit(i,0)
            if cnt <= mcnt:
                mcnt = cnt
                result = i
    print(f'#{tc} {result}')
