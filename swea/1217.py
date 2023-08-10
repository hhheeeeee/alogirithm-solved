import sys
sys.stdin = open('../../test.txt')
input = sys.stdin.readline

def power(n, m):
    if m == 1:
        return n
    return  n * power(n, m-1)

for _ in range(1 ,11):
    tc = int(input())
    N, M = map(int, input().split())
    result = power(N, M)
    print(f'#{tc} {result}')