import sys
from collections import deque
sys.stdin = open('test.txt')
input = sys.stdin.readline

for tc in range(1, 11):
    length, pwd = input().split()
    stack = []
    for c in pwd:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    print(f'#{tc} {"".join(stack)}')
