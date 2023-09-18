def Search(S, E):
    start = 0
    end = N - 1

    while start <= end:
        if stones[start] < S:
            start += 1
        elif stones[end] > E:
            end -= 1
        elif stones[start] >= S and stones[end] <= E:
            break
    return max(0, end - start + 1)

N, Q = map(int, input().split())
stones = sorted(list(map(int, input().split())))[:N] 
for _ in range(Q):
    S, E = map(int, input().split())
    print(Search(S, E))