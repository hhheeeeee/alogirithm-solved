T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    maxv = minv = start = sum(nums[:M])
    for i in range(0, N-M):
        next = start - nums[i] + nums[i+M]
        maxv = max(maxv, next)
        minv = min(minv, next)
        start = next
    print(f'#{testcase} {maxv-minv}')