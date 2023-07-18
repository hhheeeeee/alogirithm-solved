import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]
result = []

def comb(depth):
    if depth == m:
        print(*result)
        return
    
    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            comb(depth + 1)
            result.pop()

comb(0)