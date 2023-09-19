def binarySearch(target):
    start, end = 0, N # 시작 점 끝 점 초기화
    while start <= end:
        mid = (start + end) // 2
        # 1. 왼쪽 부분 탐색, 중간점의 값이 찿고자 하는 값보다 큰 경우
        if A[mid] > target:
            end = mid - 1
        # 2. 오른쪽 부분 탐색, 중간점의 값이 찾고자 하는 값보다 작은 경우
        elif A[mid]< target:
            start = mid + 1
        # 3. 탐색 종료. 중간점의 값이 찾고자 하는 값과 같은 경우
        elif A[mid] == target:
            return True
    return False


N = int(input())
A = tuple(sorted(list(map(int, input().split()))))
B = int(input())
B = tuple(map(int, input().split()))
ans = 0
for target in B:
    if binarySearch(target):
        print("O", end = "")
    else:
        print("X", end="")