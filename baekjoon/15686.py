import sys
sys.stdin = open('1.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []


def dist(house, chicken):
    d = 0
    for hx, hy in house:
        d += min([abs(cx-hx) + abs(cy-hy) for cx, cy in chicken])
    return d

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        if arr[i][j] == 2:
            chicken.append((i, j))

def subset(m, depth, start):
    global dd
    if depth == m:  # [0,1]이런식으로 오면 #chi[0] ch[1] 이렇게 뽑겟다는거임
        dd = min(dd, dist(house, [chicken[i] for i in choose]))  # 거리 계산한다
        return

    for i in range(start, L):
        choose.append(i)
        subset(m, depth+1, i+1)
        choose.pop()

L = len(chicken)
arr_c = [i for i in range(L)]

res = 10e9
# for m in range(M, 0, -1):
    # 치킨집 중에서 m개 뽑는다.
choose = []
dd = 10e9
subset(M, 0, 0)
res = min(res, dd)
print(res)
