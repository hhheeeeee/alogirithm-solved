for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    profit = 0
    for i in range(N // 2 + 1): # i : 0, 1
        profit += sum(arr[i][N // 2 - i:N // 2 + i + 1])
    for i in range(N // 2 + 1, N):
        profit += sum(arr[i][i - (N // 2) : N // 2 + (N - i)])
    print(f'#{tc} {profit}')