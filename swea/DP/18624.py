T = int(input())

day = []
pay = []

for _ in range(T):
    a, b = map(int, input().split())
    day.append(a)
    pay.append(b)

memo = [0] * (T+1)

for i in range(T-1, -1, -1):
    if i + 1 == T:
        memo[i] = pay[i]
    elif i + day[i] > T:
        memo[i] = memo[i+1]
    else:
        memo[i] = max(memo[i+1], memo[i+day[i]] + pay[i])
print(memo[0])