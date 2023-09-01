import sys
sys.stdin = open('1.txt')

N = int(input())
time = []
for i in range(N):
    s, e = map(int, input().split())
    time.append((s, e))

time = sorted(time, key = lambda x : (x[1], x[0]))
cnt = 1
end = time[0][1]
for j in range(1, N):
    if time[j][0] >= end:
        cnt += 1
        end = time[j][1]
print(cnt)
'''
4
3 3
2 3
1 3
2 2
답 : 3

4
1 4
4 4
4 4
4 5
답 : 4
'''