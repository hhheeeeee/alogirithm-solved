from collections import deque
import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

# 현재 위치에서 이동 가능한 편의점 이동가능한지 확인
# 이동가능한 편의점 q에 넣기
# 그 편의점에서 다른 편의점으로 이동
# 이동하다가 목적지 잇으면 happy~~~


def bfs(start_x, start_y, rock_x, rock_y):
    q = []
    v = [0] * n

    q.append((start_x, start_y))

    while q:
        cj, ci = q.pop(0)

        if abs(cj - rock_x) + abs(ci - rock_y) <= 1000:
            return 'happy'
        for i in range(n):
            if v[i] == 0:
                nj, ni = store[i]
                if abs(cj - nj) + abs(ci - ni) <= 1000:
                    q.append((nj, ni))
                    v[i] = 1
    return 'sad'


T = int(input())
for _ in range(T):
    n = int(input())
    start_x, start_y = map(int, input().split())
    store = []
    for _ in range(n):
        t_x, t_y = map(int, input().split())
        store.append((t_x, t_y))
    rock_x, rock_y = map(int, input().split())
    print(bfs(start_x, start_y, rock_x, rock_y))
