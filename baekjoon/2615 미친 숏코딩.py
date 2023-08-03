def check(i, j, di, dj):
    def same(ni, nj):
        return 0<=ni<19 and 0<=nj<19 and board[i][j] == board[ni][nj]
    if board[i][j] == 0: return False
    for d in range(1, 5):
        if not same(i+di*d, j+dj*d): return False
    if same(i-di, j-dj) or same(i+di*5, j+dj*5): return False
    return True

board = [list(map(int,input().split())) for i in range(19)]
for i in range(19):
    for j in range(19):
        if check(i, j, 0, 1) or check(i, j, 1, 0) or check(i, j, 1, 1) or check(i, j, -1, 1):
            print(board[i][j]); print(i+1, j+1); break
    else: continue
    break
else: print(0)