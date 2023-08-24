import sys
sys.stdin = open('../1.txt')
from collections import deque

for tc in range(1, int(input()) + 1):
    line = list(input().strip())
    madi = line[0]
    for i in range(1, len(line)):
        a = "".join(line[i: i + len(madi)])
        if a == madi:
            break
        madi += line[i]
    print(f'#{tc} {len(madi)}')
