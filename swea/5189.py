import sys
sys.stdin = open('1.txt')

def permutation(depth, N, remember, nowsum):
    global res
    if depth == N - 1:
        nowsum += arr[remember - 1][0]
        res = min(res, nowsum)
        return

    for num in arr2:
        if not visited[num]:
            visited[num] = True
            nowsum += arr[remember - 1][num - 1]
            permutation(depth + 1, N, num, nowsum)
            visited[num] = False
            nowsum -= arr[remember - 1][num - 1]


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = [i for i in range(2, N+1)]
    res = 10000000000
    visited = [False] * (N+1)
    visited[0] = True
    visited[1] = True
    permutation(0, N, 1, 0)
    # p 순열 만들고 소비량 계산하기기    print(p)
    print(f'#{tc} {res}')
