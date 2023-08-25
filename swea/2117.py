
def count_house(x, y, K):
    count = 0
    for i in range(- (K - 1), K):
        for j in range(-(K - abs(i)) + 1, K - abs(i)):
            if 0 <= x + i < N and 0 <= y + j < N:
                count += arr[x + i][y + j]

    if count * M >= (K * K) + (K - 1) * (K - 1):
        return count
    else:
        return 0

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split()) # 도시 크기, 한 집이 지불할 수 있는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxcount = 0
    K = N + 1
    while K != 0:
        for i in range(N):
            for j in range(N):
                maxcount = max(maxcount, count_house(i, j, K))
        K -= 1

    print(f'#{tc} {maxcount}')
