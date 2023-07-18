import sys
from collections import deque
sys.stdin = open('test.txt')
input = sys.stdin.readline

#비의 높이는 1~100
#높이가 바뀔 때마다 안전한 영역 개수 max값으로 갱신
#maxv값 return

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
maxv = 0

def dfs_safe(x, y,rain):
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and graph[nx][ny] > rain:
                    visited[nx][ny] = True
                    q.append((nx, ny))

for rain in range(1, 101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > rain:               
                visited[i][j] = True
                cnt += 1
                dfs_safe(i,j,rain)
    maxv = max(cnt, maxv)

print(max(1,maxv)) 

# 반례
# 2
# 1 1
# 1 1