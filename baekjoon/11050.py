import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

n, k = map(int, input().split())  # 5  2
# n C k, 5 C 2 = 5 * 4 / 2 * 1

denominator = 1
for i in range(n-k+1, n+1):
    denominator *= i

numerator = 1
for j in range(1, k+1):
    numerator *= j

print(int(denominator/numerator))
