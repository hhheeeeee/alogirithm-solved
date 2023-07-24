import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

N = int(input())
a_list = set(map(int, input().split()))
M = int(input())
b_list = list(map(int, input().split()))

for num in b_list:
    print(1 if num in a_list else 0)
