from collections import deque
import sys
sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

ERROR = -1

n = int(input())

queue = deque()

for _ in range(n):
    query = input().split()
    if query[0] == 'push':
        queue.append(query[1])
    elif query[0] == 'pop':
        print(queue.popleft() if queue else ERROR)
    elif query[0] == 'size':
        print(len(queue))
    elif query[0] == 'empty':
        print(0 if queue else 1)
    elif query[0] == 'front':
        print(queue[0] if queue else ERROR)
    elif query[0] == 'back':
        print(queue[-1] if queue else ERROR)
