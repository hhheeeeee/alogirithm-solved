import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

 
#두 기차가 부딪히기 전까지 소모된 시간 동안 파리가 움직인 거리
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    quad = 0
    for i in range(1, n):
        for j in range(1, n):
            if (i*i) + (j*j) <= (n*n):
                quad += 1
    print(f'#{tc} {(quad * 4) + (4 * n) + 1}')

    #print(f'#{tc} {D/(A+B)*F:.10f}')
    
    