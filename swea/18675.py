from collections import deque

def check(food):
    for f in food:
        if food.count(f) > 2:
            return False
    return True

for tc in range(1, int(input()) + 1):
    N, R = map(int, input().split())
    arr = list(map(int, input().split()))
    food = deque(arr[:2 * R + 1])
    res = 'YES'
    for i in range(N):
        if not check(food):
            res = 'NO'
            break
        food.append(arr[(2 * R + 1 + i) % N])
        food.popleft()
    print(f'#{tc} {res}')