import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline
# 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,
# Bi이하인 모든 정류장만을 다니는 버스 노선이다.
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    busstop = [0] * 5001
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            busstop[i] += 1
    p = int(input())
    print(f'#{tc}', end = ' ')
    for i in range(p):
        print(busstop[int(input())], end =" ")
    print()
    