import sys

sys.stdin = open('1.txt')


# 정중앙 대학교
import heapq

max_heap = []
min_heap = []

def push(v):
    if mid > v:
        heapq.heappush(max_heap, -v) # max heap 구현을 위해 -1을 곱해준다
    else:
        heapq.heappush(min_heap, v)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    push(a)
    push(b)

    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, mid)
        mid = -heapq.heappop(max_heap)
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -mid)
        mid = heapq.heappop(min_heap)
    
    print(mid)