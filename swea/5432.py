import sys
from collections import deque
sys.stdin = open('test.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    stick = []
    arr = input().strip()
    tcnt = 0
    for idx, c in enumerate(arr):
        if c == '(':
            stick.append((idx, c))
        if c == ')':
            if stick and stick[-1][1] == '(' and stick[-1][0] == idx - 1:
                stick.pop()
                tcnt += len(stick)
            elif stick and stick[-1][1] == '(' :
                stick.pop()
                tcnt += 1
    print(f'#{tc} {tcnt}')