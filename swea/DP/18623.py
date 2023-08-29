T, n = map(int, input().split())
coins = list(map(int, input().split()))
memo = [0] * (T+1)

for c in coins:
    if c <= T:
        memo[c] = 1
    else:
        print('impossible')
        exit()

for i in range(T+1):
    hubo = [memo[i - c] for c in coins if i - c >= 0 and memo[i - c] > 0]
    if hubo:
        memo[i] = min(hubo) + 1

print(memo[T] if memo[T] > 0 else 'impossible')