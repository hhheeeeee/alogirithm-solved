from collections import deque
import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

building = [0] * (F+1)


def bfs(S, G, U, D):
    q = deque([S])
    while q:
        now = q.popleft()
        if now == G:
            return building[now]
        for dir in (U, -D):
            # 방향이 0이면 무한루프!
            if dir != 0 and 0 < now + dir <= F and not building[now + dir]:
                building[now + dir] = building[now] + 1
                q.append(now + dir)

    return 'use the stairs'


print(bfs(S, G, U, D))

# 3 3 1 0 1
# answer : 2
