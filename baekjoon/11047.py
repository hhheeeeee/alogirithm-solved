import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
for i in range(N-1,-1,-1):
    if K // coins[i] > 0:
        cnt += K // coins[i]
        K -= (K // coins[i]) * coins[i]
print(cnt)

    