# 매점 수, 관객 수
N, M = map(int, input().split())
# i 번째 매점 조리 시간
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

low = 0  
high = arr[0] * M

while low <= high:
    
    mid = (low + high) // 2
    count = sum([mid // c for c in arr])
    # print(low, high, count)

    if count >=  M:
        high = mid - 1
    else:
        low = mid + 1

print(low)