import sys
sys.stdin = open('1.txt')

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    res = 0
    for i in range(100):
        line = [arr[j][i] for j in range(100) if arr[j][i] != 0]
        #앞에서부터 1이면 지우기
        i = j = 0
        while True:
            if line[i] == 1:
                break
            line.pop(0)
        #뒤에서부터 2이면 지우기
        while True:
            if line[-1] == 2:
                break
            line.pop(-1)
        # 경계선 찾기
        for i in range(len(line) - 1):
            if line[i] == 1 and line[i+1] == 2:
                res += 1
    print(f'#{tc} {res}')



