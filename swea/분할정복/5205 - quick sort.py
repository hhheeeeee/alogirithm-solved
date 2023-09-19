def quick(arr, start, end):
    if start >= end: return # 재귀 종료 조건

    pivot = start # 피벗 위치를 시작 지점으로 설정
    left = start + 1 # 왼쪽 포인터 설정
    right = end # 오른쪽 포인터 설정

    while left <= right:
        # 피벗보다 큰 값을 찾을 때까지 이동
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 값을 찾을 때까지 오른쪽 포인터로 이동
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        # 왼쪽 포인터가 오른쪽 포인터보다 크면 피벗과 오른쪽 값을 교환
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # 피벗의 왼쪽 부분 재귀적 정렬
    quick(arr, start, right - 1)
    # 피벗의 오른쪽 부분 재귀적 정렬
    quick(arr, right + 1, end)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quick(arr, 0, N-1)
    print(f'#{tc} {arr[N // 2]}')