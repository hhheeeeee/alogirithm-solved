import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N, Q = map(int, input().split())
    box = [0] * (N+1)
    for i in range(1, Q+1):
        l, r = map(int, input().split())
        for num in range(l, r+1):
            box[num] = i
    print(f'#{tc}', end = ' ')
    print(*box[1:])
    