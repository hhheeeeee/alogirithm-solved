import sys
sys.stdin = open('../1.txt')
from collections import deque

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(input().split())
    if N % 2:
        first = arr[:N // 2 + 1]
        last = arr[N // 2 + 1:]
    else:
        first = arr[:N // 2]
        last = arr[N // 2:]
    print(f'#{tc}', end =" ")
    while first or last:
        if first:
            print(first.pop(0), end = " ")
        if last:
            print(last.pop(0), end=" ")
    print()