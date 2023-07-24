import sys
sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    line = input()
    a = list(line.split())
    if a[0] == "push":
        stack.append(int(a[1]))
    elif a[0] == "pop":
        print(stack.pop(-1) if stack else -1)
    elif a[0] == "size":
        print(len(stack))
    elif a[0] == "empty":
        print(0 if stack else 1)
    elif a[0] == "top":
        print(stack[-1] if stack else -1)
