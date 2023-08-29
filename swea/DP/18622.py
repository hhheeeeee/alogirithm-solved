import sys
sys.stdin = open('1.txt')
from collections import deque



N = int(input())
arr = list(map(int, input().split()))
now = [0] * N  # 배열 크기를 N으로 변경

for i in range(N):
    if i >= 6:
        now[i] = max(now[i-2], now[i-7]) + arr[i]
    elif i % 2 == 1:
        now[i] = now[i-2] + arr[i]

print(max(now[N-7:]))
