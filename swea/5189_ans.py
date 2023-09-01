import sys
sys.stdin = open('1.txt')

def cart(cur, start, total):
    global result
    if cur == n - 1:
        result = min(result, arr[start][0]) # 총 배터리 사용량의 최소값 업데이트
        return

    for i in range(1, n):
        if visited[i] == 0 and start != 1: # 아직 방문하지 않은 구역이고, 시작구역과 다른 경우
            visited[i] = 1 # 1. 방문 표시
            cart(cur + 1, i, total + arr[start[i]]) # 2. 다음 구역으로 이동
            visited[i] = 0 # 3. 방문표시 지우기


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(n)]
    res = float('inf')
    cart(0, 0, 0)
    print(f'#{tc} {res}')
