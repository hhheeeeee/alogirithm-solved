import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def change(i):
    switch[i] = 1 - switch[i]

N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    else:
        change(num)
        for k in range(1, 1 + min(N - num, num - 1)):
            if switch[num + k] == switch[num - k]:
                change(num + k); change(num - k)
            else:
                break

for i in range(1, N+1):
    print(switch[i], end=" " if i % 20 else "\n")

# 반례 :

# 입력:
# 8
# 0 1 0 1 0 0 0 1
# 2
# 1 8
# 2 7

# 정답:
# 0 1 0 1 0 1 1 1