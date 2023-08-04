import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    tcnt = 0

    for col in range(N):
        rcnt = 0
        for row in range(N):
            if puzzle[col][row] == 1:
                rcnt +=1
            if row == N-1 or puzzle[col][row] == 0:
                if rcnt == K:
                    tcnt += 1
                rcnt = 0

    for row in range(N):
        ccnt = 0
        for col in range(N):
            if puzzle[col][row] == 1:
                ccnt +=1
            if col == N-1 or puzzle[col][row] == 0:
                if ccnt == K:
                    tcnt += 1
                ccnt = 0

    print(f'#{tc} {tcnt}')
    