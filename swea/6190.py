def isdanjo(num):
    number = str(num)
    for i in range(1, len(number)):
        if number[i] < number[i-1]:
            return -1
    return num

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            num = arr[i] * arr[j]
            if isdanjo(num) != -1:
                res = max(res, num)
    if res:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} -1')