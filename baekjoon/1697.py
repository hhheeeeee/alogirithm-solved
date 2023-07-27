from collections import deque
import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 200000


def bfs(n, k):
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            return visited[now]
        for new in (now+1, now-1, 2*now):
            # and는 앞에서부터 차례대로 검사하므로 인덱스 검사가 앞에 있어야댐!
            if 0 <= new < 100001 and not visited[new] and new != n:
                visited[new] = visited[now] + 1
                q.append(new)
    return -1


print(max(0, bfs(n, k)))


# 100 0 # 100
# 6 16 # 3
# 8 20 # 3
# 15964 89498 # 4781
# 3 43 # 6
# 4 27 # 5
# 5 35 # 5
# 6 43 # 5
# 7 43 # 6
# 100 1 # 99
# 10 19 # 2
# 5 19 # 3
# 1 20 # 5
# 100000 100000 # 0
# 0 100000 # 22
# 100000 0 # 100000
# 0 1 # 1
# 3482 45592 # 637
# 2 4 # 1
# 9 5 # 4
# 5 5 # 0
# 5 17 # 4
