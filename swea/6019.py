import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

#두 기차가 부딪히기 전까지 소모된 시간 동안 파리가 움직인 거리
T = int(input())
for tc in range(1,T+1):
    D, A, B, F = map(int, input().split())
    print(f'#{tc} {D/(A+B)*F:.10f}')
    