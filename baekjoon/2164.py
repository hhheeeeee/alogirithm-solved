import sys
from collections import deque
sys.stdin = open('test.txt')
input = sys.stdin.readline

N = int(input())

card = deque([i for i in range(1, N+1)])

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])
