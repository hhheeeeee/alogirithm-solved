import sys
sys.stdin = open('../1.txt')

from collections import deque
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    sample = deque(list(map(int, input().split())))
    passcode = deque(list(map(int, input().split())))
    result  = 1
    while sample:
        a = sample.popleft()
        if passcode and a == passcode[0]:
            passcode.popleft()
    if passcode:
        result = 0
    print(f'#{tc} {result}')
