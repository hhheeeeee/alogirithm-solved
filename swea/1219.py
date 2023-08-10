import sys
sys.stdin = open('../../test.txt')
input = sys.stdin.readline

def binary(now):
    visited[now] = True
    if left[now]:
        binary(left[now])
    if right[now]:
        binary(right[now])


for _ in range(10):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * 100
    right = [0] * 100
    visited = [0] * 100
    for i in range(N):
        start = arr[(i-1) * 2]
        end = arr[(i-1) * 2 + 1]
        if not left[start]:
            left[start] = end
        else:
            right[start] = end
    binary(0)
    if visited[99]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')



