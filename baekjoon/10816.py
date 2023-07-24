import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

N = int(input())
sg = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

hash = {}

for i in sg:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in card:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')
