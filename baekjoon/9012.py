import sys
sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

for _ in range(int(input())):
    string = input().strip()
    stack = []
    for c in string:
        if c == '(':
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            print('NO')
            break
    else:
        print('YES' if not stack else 'NO')
