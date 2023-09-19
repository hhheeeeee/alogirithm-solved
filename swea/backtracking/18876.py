def dfs(idx, sum_v):
    global answer
    # 현재 교환 횟수가 이미 찾은 정답보다 많으면 탐색 종료
    if answer < sum_v: return

    # 현재 위치가 종점 이상이면 종점에 도달한 것, 최소 교환횟수 갱신, 종료
    if idx >= N:
        answer = sum_v
        return
    
    count = station[idx] # 현재 정류장의 배터리 용량을 가져옴
    for i in range(count, 0, -1):
        if idx + 1 < N:
            dfs(idx + i, sum_v + 1) # 현재 위치에서 1만큼 이동, 교환횟수 1 증가시켜 재귀

T = int(input())
for tc in range(1,T+1):
    answer = float('inf')
    station = list(map(int, input().split()))
    N = station.pop(0) - 1
    dfs(0, -1)
    print(f'#{tc} {answer}')