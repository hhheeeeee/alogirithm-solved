import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

K = int(input())
size = 1
while size < K:
    size *= 2

size1 = size
cut = 0
while K > 0:
    if K >= size:
        K -= size
    else:
        size //= 2
        cut += 1

print(size1, cut)
        
# 4
# 4 0

# 8
# 8 0

# 17
# 32 5


