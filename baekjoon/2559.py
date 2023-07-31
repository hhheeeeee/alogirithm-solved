import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
temp = list(map(int, input().split()))

now = sum(temp[:m])
maxv = now
for i in range(0, n-m):
    new = now - temp[i] + temp[i+m]
    maxv = max(new, maxv)
    now = new

print(maxv)