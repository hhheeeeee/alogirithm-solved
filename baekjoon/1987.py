import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c: 
            if maps[nx][ny] not in alphas:
                alphas.add(maps[nx][ny])
                dfs(nx, ny, count+1)
                alphas.remove(maps[nx][ny])

alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)

# 노드(ny, nx) 가 if 분기문에 해당된다는 의미는, 
# 새롭게 노드를 뻗어나갈 수 있다는 뜻이기에 
# count 의 값을 + 1 하여 재귀호출
# dfs() 함수가 종료되면 해당 노드(ny, nx) 를 set 에서 빼줘야한다. 