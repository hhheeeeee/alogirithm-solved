n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# 투 포인터 초기화
left = 0
right = n - 1
# 변수 초기화
minv = 2e9 + 1
ansleft = 0
ansright = 0

while left < right:
    sum = arr[left] + arr[right] # 합 구하기
    if sum == 0:
        print(arr[left], arr[right])
        exit() # break와 exit() 차이
    # 절댓값을 이용해서 최소 차이를 찾기
    if minv > abs(sum):
        minv = abs(sum)
        ansleft = left
        ansright = right
    # 합이 0보다 크면 right를 줄이고, 합이 0보다 작으면 left를 줄인다
    if sum > 0: right -= 1
    else: left += 1

print(arr[ansleft], arr[ansright])