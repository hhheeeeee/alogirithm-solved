import sys
sys.stdin = open('3.txt')
input = sys.stdin.readline

# 1
T = int(input())
for tc in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()
    cnt = 0
    if str1 in str2:
        cnt += 1
    print(f'#{tc} {cnt}')

# 2
for tc in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()
    for i in range(len(str2)-len(str1)+1):
        cnt = 0
        for j in range(len(str1)):
            if str1[j] == str2[i+j]:
                cnt += 1
        if cnt == len(str1):
            result = 1