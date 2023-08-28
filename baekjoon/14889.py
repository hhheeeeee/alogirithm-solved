def power(group, arr2):
    # 만약 123같은팀이면 12 21 13 31 23 32 더해야댐
    p = 0
    for i in group:
        for j in group:
            p += arr2[i][j]
    return p

# 부분집합 만들기
def subset(idx, depth):
    global minv

    if len(start) == N // 2:
        link = [i for i in arr if i not in start]
        minv = min(abs(power(start, arr2) - power(link, arr2)), minv)
        return

    if len(start) > N // 2:
        return

    for i in range(idx, N):
        start.append(i)
        subset(i + 1, depth + 1)
        start.pop()


N = int(input())
arr = [i for i in range(0, N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
start = []
minv = 10e9
subset(0, 0)

print(minv)