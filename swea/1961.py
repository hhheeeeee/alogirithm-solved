import sys
from collections import deque
sys.stdin = open('test.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    print(f'#{tc}')
    for k in range(n):
        print("".join([arr[i][k] for i in range(n - 1, -1, -1)]), end=" ")
        print("".join([arr[n - 1 - k][i] for i in range(n - 1, -1, -1)]), end=" ")
        print("".join([arr[i][n - 1 - k] for i in range(n)]))

