import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    result = []
    for _ in range(5):
        result.append(max(nums))
        result.append(min(nums))
        nums.remove(max(nums))
        nums.remove(min(nums))
    print(f'#{tc}', *result)



