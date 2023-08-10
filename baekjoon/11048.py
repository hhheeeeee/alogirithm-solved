import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
candy = [[0] * M for _ in range(N)]
#초기화
for i in range(M):
    candy[0][i] = sum(maze[0][:i+1])
for i in range(N):
    candy[i][0] = maze[i][0] + candy[i-1][0]

for i in range(1, N):
    for j in range(1, M):
        candy[i][j] = max(candy[i-1][j-1], candy[i-1][j], candy[i][j-1]) + maze[i][j]

print(candy[N-1][M-1])
