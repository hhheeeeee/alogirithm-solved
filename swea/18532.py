import sys

sys.stdin = open('../1.txt')

def calcul(ans, student):
    score, total = 0, 0
    for i in range(M):
        if ans[i] == student[i]:
            score += 1
            total += score
        else:
            score = 0
    return total


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    ans = list(map(int, input().split()))
    students = [list(map(int, input().split())) for _ in range(N)]
    maxv = 0
    minv = 10*6
    for stu in students:
        minv = min(minv, calcul(ans, stu))
        maxv = max(maxv, calcul(ans, stu))
    print(f'#{tc} {maxv - minv}')
