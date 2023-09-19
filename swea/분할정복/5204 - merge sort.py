# 분할 함수
def divide(arr):
    if len(arr) <= 1: # 리스트의 길이가 1이하면 그대로 반환
        return arr
    mid = len(arr) // 2
    left = divide(arr[:mid]) # 왼쪽 부분
    right = divide(arr[mid:]) # 오른쪽 부분
    return merge(left, right)

# 병합 함수
def merge(left, right):
    global ans
    # 왼쪽 리스트의 마지막 원소가 오른쪽 리스트의 마지막 원소보다 큰 경우 ans1 증가
    if right[-1] < left[-1]:
        ans += 1
    result = [] # 병함 결과
    len_l = len(left)
    len_r = len(right)
    l = r = 0
    while l < len_l or r < len_r:
        # 1. 왼쪽과 오른쪽 리스트 모두 남아있는 경우
        if l < len_l and r < len_r:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        # 2. 오른쪽 리스트만 남아 있는 경우
        elif l < len_l:
            result.append(left[l])
            l += 1
        # 3. 왼쪽 리스트만 남아 있는 경우
        elif r < len_r:
            result.append(right[r])
            r += 1
    
    return result



for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    result = divide(arr)
    print(f'#{tc} {result[N // 2]} {ans}')