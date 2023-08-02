import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

T = int(input())

if T % 2 == 0:
    first = "* " * (T // 2)
else:
    first = "* " * (T // 2 + 1)
second = " *" * (T // 2)

for _ in range(T):
    print(first)
    print(second)
