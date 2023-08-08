
import sys
sys.stdin = open('3.txt', encoding='UTF8')
input = sys.stdin.readline

for _ in range(10):
    tc = int(input())
    key = input().strip()
    t = input().strip()
    tcnt = 0
    for i in range(len(t) - len(key) + 1):
        wlen = 0
        for j in range(len(key)):
            if t[i+j] == key[j]:
                wlen += 1
        if wlen == len(key):
            tcnt += 1
    print(f'#{tc} {tcnt}')