def binarySearch(target):
    global direction
    low = 0
    high = len(arr) - 1

    # low > high 라면 데이터를 데이터를 못 찾은 경우
    while low <= high:
        mid = (low + high) // 2

        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            return mid
        # 2. 가운데 값이 정답보다 작은 경우
        elif arr[mid] < target:
            if direction != 2:
                low = mid + 1
                direction = 2
            else:
                return -1
        # 3. 가운데 값이 정답보다 큰 경우
        else:
            if direction != 1:
                high = mid - 1
                direction = 1
            else:
                return -1

    return -1

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    B  = list(map(int, input().split()))
    cnt = 0
    for target in B:
        direction = 0
        if binarySearch(target) != -1:
                cnt += 1
    print(f'#{tc} {cnt}')