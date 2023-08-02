import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def binary(lower, upper, search):
    cnt = 0
    while lower < upper:
    # 책이 총 400, search = 300
        mid = int((lower + upper) / 2)
        if mid > search:
            upper = mid
            cnt += 1
        if mid < search:
            lower = mid
            cnt += 1
        else:
            return cnt
    return cnt

T = int(input())
for tc in range(1, T+1):
    upper, A, B = map(int, input().split())
    A_result, B_result = binary(1, upper, A), binary(1, upper, B)
    if A_result < B_result:
        result = 'A'
    elif A_result > B_result:
        result = 'B'
    else:
        result = 0
    print(f'#{tc} {result}')



