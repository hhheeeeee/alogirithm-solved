import sys
import itertools
sys.stdin = open('test.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    sx, sy, ex, ey = arr[0], arr[1], arr[2], arr[3]
    cust = []
    for i in range(4, n*2 + 4, 2):
        cust.append((arr[i], arr[i+1]))
    mind = 100000
    for c in itertools.permutations(cust, n):
        b = [(sx, sy)] + list(c) + [(ex, ey)]
        dist = 0
        for i in range(n+1):
            dist += abs(b[i][0] - b[i+1][0]) + abs(b[i][1] - b[i+1][1])
        mind = min(dist, mind)
    print(f'#{tc} {mind}')