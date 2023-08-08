import sys
sys.stdin = open('3.txt')
input = sys.stdin.readline

def BruteForce(to_find, t):
    M = len(to_find)
    N = len(t)
    i = 0 # t의 인덱스
    j = 0 # to_find의 인덱스
    while j < M and i < N:
        if t[i] != to_find[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    
    if j == M:
        return 1 # 검색 성공
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()
    result = BruteForce(str1, str2)
    print(f'#{tc} {result}')