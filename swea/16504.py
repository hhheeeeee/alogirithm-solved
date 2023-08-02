import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def gravity(boxs):
    maxv = 0
    for now, box in enumerate(boxs):
        fall = 0
        for next in range(now + 1, n):
            if box > boxs[next]:
                fall += 1
        maxv = max(maxv, fall)
    return maxv


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    boxs = list(map(int, input().split()))
    print(f'#{tc} {gravity(boxs)}')