import sys
sys.stdin = open('a.txt')
input = sys.stdin.readline
# N=2a x 3b x 5c x 7d x 11e
# N이 주어질 때 a, b, c, d, e 를 출력하라.

def divide(N, num):
    i = 0
    while True:
        if N % num != 0:
            return i
        N /= num
        i += 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc} ', end = '')
    for num in [2, 3, 5, 7, 11]:
        print(divide(N, num), end = ' ')
    print()