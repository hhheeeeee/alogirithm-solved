import sys
sys.stdin = open('3.txt')
input = sys.stdin.readline

# 1번 방법
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    maxv = 0
    for i in str1:
        maxv = max(maxv, str2.count(i))
    print(f'#{tc} {maxv}')


# 2번 방법
T = int(input())
for tc in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()
    alpha = dict()
    for i in str2:
        alpha[i] = 0
    for i in str2:
        alpha[i] += 1
    maxv = 0
    for i in str1:
        if i in alpha.keys():
            if alpha[i] > maxv:
                maxv = alpha[i]
    print(maxv)
