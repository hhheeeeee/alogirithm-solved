def move(K, N, M, charge_point):
    now, charge = 0, 0
    stops = [0] * (N+1)
    for i in charge_point:
        stops[i] += 1
    while True:
        if now >= N:
            break
        for i in range(K,0,-1):
            if now + i >= N:
                return charge
            if now + i <= N and stops[now + i] == 1:
                now += i
                charge += 1
                break
        else:
            return 0
    

T = int(input())
for testcase in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_point = list(map(int, input().split()))
    print(f'#{testcase} {move(K, N, M, charge_point)}')

