import sys
from collections import deque

sys.stdin = open('input.txt')  # 적절한 입력 파일 경로로 변경해주세요.
input = sys.stdin.readline

from collections import deque

A = list(input().strip())
B = list(input().strip())

while len(A) < len(B):
    if B:
        if B[-1] == 'A':
            B.pop(-1)
        else:
            B.pop(-1)
            B.reverse()
            

if A == B:
    print(1)
else:
    print(0)


'''
https://www.acmicpc.net/board/view/83783

ABB
BBAB
1

BAAB
BBAABBAAAAAAAA
1

AAB
BABBAABBBAAAAABAA
1
'''