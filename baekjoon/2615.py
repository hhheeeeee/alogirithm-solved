import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def search(i, j, dy, dx, color):
    count = 1
    ii, jj = i, j # 시작 위치 기억
    for k in range(1,5):
        ni = i + dy * k
        nj = j + dx * k
        if not (0<=ni<19) or not (0<=nj<19):
            return False
        if board[ni][nj] != color:
            return False
        count += 1
    else:
        if count == 5: #만약 오목 5개 연속을 찾았다면
            # 그 이전이랑 그 이후 확인, 둘 다 해당 하는 색 아니어야 됨
            # 만약에 그 이전이 오목 안이라면, 그 색이 아니어야 됨
            if 0<=(ii-dy)<19 and 0<=(jj-dx)<19:
                if board[ii-dy][jj-dx] == color:
                    return False
            # 그 이후가 오목 안이라면, 그 색이 아니어야 됨
            if 0<=ni + dy<19 and 0<=nj + dx<19:
                if board[ni + dy][nj + dx] == color:
                    return False
            return True                    
        
        else:
            return False

board = [list(map(int, input().split())) for _ in range(19)]
color = 0
ry, rx = 0, 0
flag = 0
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            for dy, dx in [(1, 0), (0, 1),(1, 1),(-1,1)]:
                ry, rx = i, j # 시작 위치 기억
                if search(i, j, dy, dx, board[i][j]):
                    flag = 1
                    color = board[ry][rx]
                    print(color)
                    print(ry+1, rx+1)
if flag == 0:
    print(0)

