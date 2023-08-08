
import sys
sys.stdin = open('3.txt', encoding='UTF8')
input = sys.stdin.readline

def is_palin(string):
    if string == string.reverse():
        return True
    return False

# for _ in range(10):
#     M = int(input())
#     board = [list(input().strip()) for _ in range(8)]
#     tcnt = 0
#     for i in range(8-M):
#         for j in range(8-M):
#             #열 체크
#             print(board[i][j:j+M])
#             if is_palin(board[i][j:j+M]):
#                 tcnt += 1
#             # 행 체크
#             a = [board[i + k][j] for k in range(M)]
#             print(a)
#             if is_palin(a):
#                 tcnt += 1
#     print(tcnt)




a = ['A', 'C', 'A','D']
a.reverse()
print(a)
b = a.reverse()
print(b)